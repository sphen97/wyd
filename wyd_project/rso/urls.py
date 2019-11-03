from django.urls import path
from .views import (
  RSOCreateView
)
from . import views

urlpatterns = [
  path('rso/create', RSOCreateView.as_view(), name='rso-create')
]