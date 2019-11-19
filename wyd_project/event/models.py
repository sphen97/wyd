import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from rso.models import RSO
from university.models import University


class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Going to need to add Lattitude + Longitude stuff here

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    public = models.BooleanField(default=False)
    rso = models.ForeignKey(RSO, on_delete=models.CASCADE, null=True, blank=True)
    place = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    date_posted = models.DateTimeField(default=timezone.now, null=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name = 'comments')
    date_posted = models.DateTimeField(default=timezone.now)
    rating = models.SmallIntegerField()
    text = models.TextField()

    class Meta:
        ordering = ['-date_posted']