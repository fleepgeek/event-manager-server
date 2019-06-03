from django.urls import path

from .views import UserDetailAPIView, UserEventAPIView, UserEventAttendingListView

app_name = 'accounts.user'
urlpatterns = [
    path('<int:pk>/', UserDetailAPIView.as_view(), name='detail'),
    path('<int:pk>/events/', UserEventAPIView.as_view(), name='event-list'),
    path('<int:pk>/attending/', UserEventAttendingListView.as_view(), name='attending-list'),
]