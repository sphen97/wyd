import datetime
from django import forms
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import ModelFormMixin
from django.views.generic import (
  CreateView,
  ListView
)
from users.models import Profile
from event.models import Event
from event.models import University
from .forms import RSOForm, JoinForm
from .models import RSO
from django.db.models import Q

@login_required
def rso_create(request):
  if request.method == 'POST':
      form = RSOForm(request.POST, request.FILES, instance=request.user)
      if form.is_valid():
          obj = RSO()
          obj.admin = request.user
          obj.name = form.cleaned_data['name']
          obj.description = form.cleaned_data['description']
          obj.university = get_object_or_404(Profile, user=request.user).university
          obj.approved = False
          obj.save()
          obj.members.add(request.user)
          obj.members.add(User.objects.all().get(email=form.cleaned_data['first_member']))
          obj.members.add(User.objects.all().get(email=form.cleaned_data['second_member']))
          obj.members.add(User.objects.all().get(email=form.cleaned_data['third_member']))
          obj.members.add(User.objects.all().get(email=form.cleaned_data['fourth_member']))
          username = form.cleaned_data.get('username')
          obj.save()
          messages.success(request, f'Your RSO request was sucessfully submited! Please wait for an admin to approve.')
          return redirect('event-home')
  else:
      form = RSOForm()
  return render(request, 'rso/create.html', {'form': form})

class RSOListView(LoginRequiredMixin, ListView):
    model = RSO
    template_name = 'rso/rso_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'RSOs'
    ordering = ['name']
    paginate_by = 5

    def get_queryset(self):
        myuser = get_object_or_404(User, username=self.kwargs.get('username'))
        myprofile = get_object_or_404(Profile, user=myuser)

        return RSO.objects.all().filter(university=myprofile.university)

def join_rso(request, pk):
  rso = get_object_or_404(RSO, pk=pk)
  rso.members.add(request.user)
  messages.success(request, f'Your successfully joined an RSO!')
  return redirect('event-home')
