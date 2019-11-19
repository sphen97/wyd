from django.urls import path
from .views import RSOListView
from rso import views as view

urlpatterns = [
  path('rso/create/', view.rso_create, name='rso-create')
]