import datetime
from django import forms
from django.contrib.auth.models import User
from rso.models import RSO
from .models import Event

class CreateEventForm(forms.ModelForm):

  class Meta:
    model = Event
    fields = ['title', 'date', 'time', 'rso', 'place', 'description']


  
  def __init__(self, *args, **kwargs):
    super(CreateEventForm, self).__init__(*args, **kwargs)
    user = kwargs.pop('instance', User)
    self.fields['rso'].queryset = RSO.objects.all().filter(members__pk=user.pk)