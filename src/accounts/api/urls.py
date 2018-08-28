from django.urls import path

from accounts.api import views

app_name = 'accounts'
urlpatterns = [
    # path('<int:id>/', views.EventDetailAPIView.as_view(), name='detail'),
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('', views.LoginAPIView.as_view(), name='login'),
]
