from django.urls import path

from .views import UserDetailAPIView, UserEventAPIView, UserEventAttendingListView

app_name = 'accounts.user'
urlpatterns = [
    path('<str:username>/', UserDetailAPIView.as_view(), name='detail'),
    path('<str:username>/event/', UserEventAPIView.as_view(), name='event-list'),
    path('<str:username>/attending', UserEventAttendingListView.as_view(), name='attending-list'),
]