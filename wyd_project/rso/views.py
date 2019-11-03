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

@login_required
def rso_create(request):
  if request.method == 'POST':
    form = RSOForm(request.POST, instance=request.user)
    if form.is_valid():
      form.instance.approved = False
      form.save(commit=True)
      messages.success(request, f'An RSO Request has been submitted!')
      return redirect('event-home')
  else:
    form = RSOForm(instance=request.user)
    
  return render(request, 'rso/create.html', {'form' : form})