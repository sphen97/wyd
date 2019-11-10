from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from university.models import University


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    schoolFound = False
    if created:
        for school in University.objects.all():
            if instance.email.endswith(school.domain):
                Profile.objects.create(user=instance, university=school)
                schoolFound = True
                break
        if not schoolFound:
            Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
