from django import forms
from django.contrib.auth.models import User
from .models import RSO

class RSOForm(forms.ModelForm):
  # name = forms.CharField(max_length=75, required=True)
  # description = forms.Textarea()
  # first_member = forms.EmailField()
  # second_member = forms.EmailField()
  # third_member = forms.EmailField()
  # fourth_memeber = forms.EmailField()

  members = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple)

  class Meta:
    model = RSO
    fields = ['name', 'description', 'members']