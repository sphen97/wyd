from django.urls import path
from .views import (
    EventListView,
    EventDetailView,
    # EventCreateView,
    # EventUpdateView,
    EventDeleteView,
    UserEventListView,
    RSOEventListView
)
from . import views
from . import views as view

urlpatterns = [
    path('', EventListView.as_view(), name='event-home'),
    path('home/', EventListView.as_view(), name='event-home'),
    path('user/<str:username>', UserEventListView.as_view(), name='user-events'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/new/', view.create_event, name='event-create'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
    path('about/', views.about, name='event-about'),
    path('rso/<int:pk>/', RSOEventListView.as_view(), name='rso-events'),
    path('event/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]
