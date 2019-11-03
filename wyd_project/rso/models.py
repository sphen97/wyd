from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class RSO(models.Model):
  name = models.CharField(max_length=75)
  admin = models.ForeignKey(User, on_delete=models.PROTECT, related_name='admin')
  members = models.ManyToManyField(to = User)
  description = models.TextField()
  approved = models.BooleanField()

  def __str__(self):
    return self.name