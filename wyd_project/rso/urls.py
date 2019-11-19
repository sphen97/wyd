from django.urls import path
from .views import (
  RSOEventListView,
  RSOCreateView
)

urlpatterns = [
  path('rso/create/', RSOCreateView.as_view(), name='rso-create'),
]