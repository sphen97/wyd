from django.urls import path
from .views import (
    EventListView,
    EventDetailView,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
    UserEventListView
)
from . import views

urlpatterns = [
    path('', EventListView.as_view(), name='event-home'),
    path('user/<str:username>', UserEventListView.as_view(), name='user-events'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/new/', EventCreateView.as_view(), name='event-create'),
    path('event/<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
    path('about/', views.about, name='event-about'),
]
