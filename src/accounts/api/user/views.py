from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserDetailSerializer
from accounts.api.serializers import UserPublicSerializer
from event.models import Event, Attendee
from event.api.serializers import EventInlineUserSerializer, EventSerializer
from event.api.views import EventAPIView
from accounts.api.permissions import IsOwnerOrReadOnly

User = get_user_model()

class UserDetailAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    lookup_field = 'pk'

class UserEventAPIView(EventAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EventInlineUserSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('pk')
        qs = Event.objects.filter(creator__pk=user_id)
        return qs

    def post(self, request, *args, **kwargs):
        return Response({'detail': 'Post not allowed in this url'}, status=400)


class UserEventAttendingListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EventSerializer
    
    def get_queryset(self):
        user_id = self.kwargs.get('pk')
        qs = Event.objects.filter(attendee__user__pk=user_id)
        return qs
    