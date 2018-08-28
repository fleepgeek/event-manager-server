from rest_framework import generics, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from event.models import Event, Attendee
from .serializers import EventSerializer, AttendeeSerializer
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


# class AttendeeAPIView(generics.CreateAPIView):
#     permission_classes = []
#     serializer_class = AttendeeSerializer
#     queryset = Attendee.objects.all()

class AttendeeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        event_id = self.kwargs.get('id')
        qs = Event.objects.filter(id=event_id)
        if qs.exists():
            event = qs.first()
            user = request.user
            has_registered = Attendee.objects.is_registered(event=event, user=user)
            if has_registered:
                return Response({'detail': 'You have previously registered for this event'}, status=400)
            else:
                Attendee.objects.create(event=event, user=user)
                return Response({'detail': 'You have successfully registered for this event'})

        return Response({'detail': 'This Event does not exists'}, status=404)