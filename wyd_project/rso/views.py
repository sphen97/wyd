import datetime
from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import ModelFormMixin
from django.views.generic import (
  CreateView
)
from .forms import RSOForm
from .models import RSO

@login_required
def rso_create(request):
  if request.method == 'POST':
    form = RSOForm(request.POST, instance=request.user)
    if form.is_valid():
      instance = RSO.objects.create(name=form.cleaned_data['name'],
                                    admin=request.user,
                                    description=form.cleaned_data['description'],
                                    approved=False)

      instance.members.set(form.cleaned_data['members'])
      instance.save()

      messages.success(request, f'An RSO Request has been submitted!')

      return redirect('event-home')
  else:
    form = RSOForm(instance=request.user)
    
  return render(request, 'rso/create.html', {'form' : form})