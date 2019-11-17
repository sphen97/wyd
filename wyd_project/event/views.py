from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
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
from .models import Comment
from .forms import CreateEventForm , CommentForm
from users.models import Profile
from rso.models import RSO


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
            obj.university = Profile.objects.get(user=request.user).university
            obj.place = form.cleaned_data['place']
            obj.description = form.cleaned_data['description']
            obj.date_posted = timezone.now()

            if obj.rso.admin == request.user:
                obj.approved = True

            obj.save()
            messages.success(request, f'Your event has been created!')
            return redirect('event-home')
    else:
        form = CreateEventForm(None, instance=request.user )
    return render(request, 'event/event_form.html', {'form': form})

class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'event/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'Events'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        profile = get_object_or_404(Profile, user=self.request.user)
        school = profile.university

        events = Event.objects.none()

        for myRSO in RSO.objects.all().filter(members__pk=self.request.user.pk):
            events = events.union(Event.objects.filter(Q(approved=True) & Q(rso=myRSO)))

        return events.union(Event.objects.filter(Q(approved=True) & (Q(public=True) | Q(university=school) & Q(rso__isnull=True))))


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


def add_comment_to_post(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.event = event
            comment.rating = form.cleaned_data['rating']
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('event-detail', pk=event.pk)
    else:
        form = CommentForm()
    return render(request, 'event/add_comment_to_post.html', {'form': form})
