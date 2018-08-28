from django.urls import path

from .views import UserEventAPIView

app_name = 'accounts.user'
urlpatterns = [
    # path('<str:username>/', UserDetailAPIView.as_view(), name='detail'),
    # path('<str:username>/status/', UserStatusAPIView.as_view(), name='status-list'),
    path('<str:username>/event/', UserEventAPIView.as_view(), name='events-list'),
]