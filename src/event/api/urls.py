from django.urls import path

from event.api import views

app_name = 'event'
urlpatterns = [
    path('<int:id>/', views.EventDetailAPIView.as_view(), name='detail'),
    path('', views.EventAPIView.as_view(), name='list'),
]