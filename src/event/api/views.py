from rest_framework import generics, mixins, permissions

from event.models import Event
from .serializers import EventSerializer
from accounts.api.permissions import IsOwnerOrReadOnly

class EventAPIView(generics.CreateAPIView, generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    lookup_field = 'id'