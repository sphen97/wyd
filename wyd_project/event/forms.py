import datetime
from django import forms
from django.contrib.auth.models import User
from django.forms import SelectDateWidget
from rso.models import RSO
from .models import Event
from .models import Comment
from django.forms import TimeInput

from location_field.forms.plain import PlainLocationField

class CreateEventForm(forms.ModelForm):
    date = forms.DateField(
        widget=SelectDateWidget()
    )
    time = forms.TimeField(widget=forms.TextInput(attrs={'placeholder': '12:00 AM -> 11:59 PM'}))

    class Meta:
        model = Event
        fields = ['title', 'date', 'time', 'public', 'rso', 'place', 'description']

    def __init__(self, *args, **kwargs):
        super(CreateEventForm, self).__init__(*args, **kwargs)
        user = kwargs.pop('instance', User)
        self.fields['rso'].queryset = RSO.objects.all().filter(members__pk=user.pk)


#commenting form for events
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('rating', 'text',)
