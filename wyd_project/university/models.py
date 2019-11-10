from django.db import models

# Create your models here.
class University(models.Model):
  name = models.CharField(max_length=75)
  description = models.TextField()
  population = models.PositiveIntegerField()
  domain = models.CharField(max_length=50)

  def __str__(self):
    return self.name