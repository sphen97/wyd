from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

def has_user_account(value):
  try:
    User.objects.all().get(email=value)
    return value
  except User.DoesNotExist:
    raise ValidationError("This email does not have an associated user account!")