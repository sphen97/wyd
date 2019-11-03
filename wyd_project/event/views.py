from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Event
from .forms import CreateEventForm

def home(request):
    context = {
        'Events': Event.objects.all()
    }
    return render(request, 'event/home.html', context)

@login_required
def create_event(request):
    if request.method == 'POST':
        form = CreateEventForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            obj = Event()
            obj.title = form.cleaned_data['title']
            obj.date = form.cleaned_data['date']
            obj.time = form.cleaned_data['time']
            obj.rso = form.cleaned_data['rso']
            obj.host = request.user
            obj.place = form.cleaned_data['place']
            obj.description = form.cleaned_data['description']
            obj.date_posted = timezone.now()
            obj.save()
            messages.success(request, f'Your event has been created!')
            return redirect('event-home')
    else:
        form = CreateEventForm(None, instance=request.user )
    return render(request, 'event/event_form.html', {'form': form})

class EventListView(ListView):
    model = Event
    template_name = 'event/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'Events'
    ordering = ['-date_posted']
    paginate_by = 5


class EventDetailView(DetailView):
    model = Event


# class EventCreateView(LoginRequiredMixin, CreateView):
#     model = Event
#     fields = ['title', 'date', 'time', 'place', 'description']

#     def form_valid(self, form):
#         form.instance.host = self.request.user
#         form.fields['date'].widget = forms.DateField()
#         form.fields['time'].widget = forms.TimeField()
#         return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super().form_valid(form)

    def test_func(self):
        event = self.get_object()
        if self.request.user == Event.host:
            return True
        return False


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/'

    def test_func(self):
        event = self.get_object()
        if self.request.user == Event.host:
            return True
        return False

class UserEventListView(ListView):
    model = Event
    template_name = 'event/user_events.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'events'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Event.objects.filter(host=user).order_by('-date_posted')


def about(request):
    return render(request, 'event/about.html', {'title': 'About'})
