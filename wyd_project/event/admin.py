from django.contrib import admin
from .models import Comment, Event, Location

admin.site.register(Comment)
admin.site.register(Event)
admin.site.register(Location)