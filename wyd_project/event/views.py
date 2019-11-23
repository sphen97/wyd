import datetime
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
from .models import Location, Place
from .forms import CreateEventForm , CommentForm
from users.models import Profile
from rso.models import RSO
from university.models import University
from django.core.mail import send_mail


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
            obj.public = form.cleaned_data['public']
            obj.rso = form.cleaned_data['rso']
            obj.host = request.user
            obj.university = Profile.objects.get(user=request.user).university
            obj.place = form.cleaned_data['place']
            obj.description = form.cleaned_data['description']
            obj.date_posted = timezone.now()

            if obj.rso != None:
                if obj.rso.admin == request.user:
                    obj.approved = True
            elif request.user.is_superuser:
                obj.approved = True
            else:
                obj.approved = False

            obj.save()

            if obj.approved == True:
                for user in obj.rso.members.all():
                    send_mail(
                        obj.title,
                        obj.description,
                        obj.rso.admin.email,
                        [user.email],
                        fail_silently=True,
                    )

            messages.success(request, f'Your event has been created!')
            return redirect('event-home')
    else:
        form = CreateEventForm(None, instance=request.user )
    return render(request, 'event/event_form.html', {'form': form})

class PlaceCreateView(CreateView):
    model = Place
    template_name = 'event/coord_update_form.html'
    success_url = '/'
    fields = ('city', 'location',)

    def set_coords(request):
        if request.method == 'POST':
            obj = Event()
            obj.coord = model.location
            obj.save()
            messages.success(request, f'Location coordinates have been saved!')
            return redirect('event-home')

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
        startdate=datetime.date.today()
        enddate=datetime.date.max
        return events.union(
            Event.objects.filter(
                Q(approved=True) & (Q(public=True) | 
                Q(university=school) & Q(rso__isnull=True)
                )
            )
        ).intersection(Event.objects.filter(date__range=[startdate, enddate])).order_by('time').order_by('date')


class EventDetailView(DetailView):
    model = Event

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'event/event_confirm_delete.html'
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
        profile = get_object_or_404(Profile, user=self.request.user)
        school = profile.university

        events = Event.objects.none()

        for myRSO in RSO.objects.all().filter(members__pk=self.request.user.pk):
            events = events.union(Event.objects.filter(Q(approved=True) & Q(rso=myRSO)))

        permitted_events = events.union(
            Event.objects.filter(
                Q(approved=True) & (Q(public=True) | Q(university=school) & Q(rso__isnull=True))
            )
        )
        return permitted_events.intersection(Event.objects.filter(host=user)).order_by('time').order_by('date')


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

class RSOEventListView(ListView, LoginRequiredMixin, UserPassesTestMixin):
    model = Event
    template_name = 'event/rso_events.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'events'
    paginate_by = 5
    
    #NOT WORKING!!!
    def test_func(self):
        myRSO = get_object_or_404(RSO, pk=self.kwargs.get('pk'))
        if myRSO.members.get(User=self.pk):
            return True
        return False

    def get_queryset(self):
        myRSO = get_object_or_404(RSO, pk=self.kwargs.get('pk'))

        return Event.objects.filter(
            Q(approved=True) & Q(rso=myRSO)
            ).order_by('time').order_by('date')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['rso'] = get_object_or_404(RSO, pk=self.kwargs.get('pk'))
        return data


class UniversityEventListView(ListView, LoginRequiredMixin, UserPassesTestMixin):
    model = Event
    template_name = 'event/university_events.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'events'
    paginate_by = 5
    
    #NOT WORKING!!!
    def test_func(self):
        myUniversity = get_object_or_404(University, pk=self.kwargs.get('pk'))
        if myUniversity.members.get(User=self.pk):
            return True
        return False

    def get_queryset(self):
        myUniversity = get_object_or_404(University, pk=self.kwargs.get('pk'))
        return Event.objects.filter(Q(approved=True) & Q(university=myUniversity)).order_by('time').order_by('date')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['university'] = get_object_or_404(University, pk=self.kwargs.get('pk'))
        return data


class CommentDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    template_name = 'event/comment_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        comment = self.get_object()
        if self.request.user == Comment.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        my_comment = get_object_or_404(Comment, pk=self.kwargs.get('pk'))
        data['event'] = my_comment.event
        return data