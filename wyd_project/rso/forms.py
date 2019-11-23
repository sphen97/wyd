from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import RSO
from .validators import has_user_account

class RSOForm(forms.ModelForm):
  name = forms.CharField(max_length=75, required=True)
  description = forms.Textarea()
  first_member = forms.EmailField()
  second_member = forms.EmailField()
  third_member = forms.EmailField()
  fourth_member = forms.EmailField()

  def clean(self):
    form_data = self.cleaned_data

    # Check fourth_member
    if form_data['fourth_member'] == self.user.email:
      self._errors['fourth_member'] = ["You will already be a member!"] # Will raise a error message
      del form_data['fourth_member']
    elif form_data['fourth_member'] == form_data['first_member']:
      self._errors['fourth_member'] = ["Cannot have the same member multiple times!"] # Will raise a error message
      del form_data['fourth_member']
    elif form_data['fourth_member'] == form_data['second_member']:
      self._errors['fourth_member'] = ["Cannot have the same member multiple times!"] # Will raise a error message
      del form_data['fourth_member']
    elif form_data['fourth_member'] == form_data['third_member']:
      self._errors['fourth_member'] = ["Cannot have the same member multiple times!"] # Will raise a error message
      del form_data['fourth_member']
    # Checking Domain
    elif self.user.email.split('@')[-1] != form_data['fourth_member'].split('@')[-1]:
      self._errors['fourth_member'] = ["Must have the same email domain as you!"]
      del form_data['fourth_member']
    else:
      try: User.objects.all().get(email=form_data['fourth_member'])
      except User.DoesNotExist:
        self._errors['fourth_member'] = ["This email does not have an associated user account!"]
        del form_data['fourth_member']

    # Check third_member
    if form_data['third_member'] == self.user.email:
      self._errors['third_member'] = ["You will already be a member!"] # Will raise a error message
      del form_data['third_member']
    elif form_data['third_member'] == form_data['first_member']:
      self._errors['third_member'] = ["Cannot have the same member multiple times!"] # Will raise a error message
      del form_data['third_member']
    elif form_data['third_member'] == form_data['second_member']:
      self._errors['third_member'] = ["Cannot have the same member multiple times!"] # Will raise a error message
      del form_data['third_member']
    # Checking Domain
    elif self.user.email.split('@')[-1] != form_data['third_member'].split('@')[-1]:
      self._errors['third_member'] = ["Must have the same email domain as you!"]
      del form_data['third_member']
    else:
      try: User.objects.all().get(email=form_data['third_member'])
      except User.DoesNotExist:
        self._errors['third_member'] = ["This email does not have an associated user account!"]
        del form_data['third_member']

    # Check third_member
    if form_data['second_member'] == self.user.email:
      self._errors['second_member'] = ["You will already be a member!"] # Will raise a error message
      del form_data['second_member']
    elif form_data['second_member'] == form_data['first_member']:
      self._errors['second_member'] = ["Cannot have the same member multiple times!"] # Will raise a error message
      del form_data['second_member']
    #Checking Domain
    elif self.user.email.split('@')[-1] != form_data['second_member'].split('@')[-1]:
      self._errors['second_member'] = ["Must have the same email domain as you!"]
      del form_data['second_member']
    else:
      try: User.objects.all().get(email=form_data['second_member'])
      except User.DoesNotExist:
        self._errors['second_member'] = ["This email does not have an associated user account!"]
        del form_data['second_member']

    #Checking Domain of user 1
    if form_data['first_member'] == self.user.email:
      self._errors['first_member'] = ["You will already be a member!"] # Will raise a error message
      del form_data['first_member']
    elif self.user.email.split('@')[-1] != form_data['first_member'].split('@')[-1]:
      self._errors['first_member'] = ["Must have the same email domain as you!"]
      del form_data['first_member']
    else:
      try: User.objects.all().get(email=form_data['first_member'])
      except User.DoesNotExist:
        self._errors['first_member'] = ["This email does not have an associated user account!"]
        del form_data['first_member']

    return form_data

  def __init__(self, *args, **kwargs):
    super(RSOForm, self).__init__(*args, **kwargs)
    self.user = kwargs.pop('instance', User)

  class Meta:
    model = RSO
    fields = ['name', 'description']

class JoinForm(forms.ModelForm):
  class Meta:
    module = RSO