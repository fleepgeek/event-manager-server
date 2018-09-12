from django.urls import path

from event.api import views

app_name = 'event'
urlpatterns = [
    path('<int:id>/attendees/', views.EventAttendeesAPIView.as_view(), name='attendees'),
    path('<int:id>/attend/', views.AttendeeAPIView.as_view(), name='attend'),
    path('<int:id>/', views.EventDetailAPIView.as_view(), name='detail'),
    path('', views.EventAPIView.as_view(), name='list'),
]
