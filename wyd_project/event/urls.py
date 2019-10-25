from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='event-home'),
    path('event/', views.about, name='event-about'),
]
