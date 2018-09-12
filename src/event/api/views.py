from django.contrib.auth import get_user_model

from rest_framework import generics, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.api.serializers import UserPublicSerializer
from event.models import Event, Attendee
from .serializers import EventSerializer
from accounts.api.permissions import IsOwnerOrReadOnly

User = get_user_model()

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

class AttendeeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        event_id = self.kwargs.get('id')
        qs = Event.objects.filter(id=event_id)
        if qs.exists():
            event = qs.first()
            user = request.user
            print(event.creator)
            if event.creator == user:
                return Response({'detail': 'No need for this. You are the creator of this event'}, status=401)
            has_registered = Attendee.objects.is_registered(event=event, user=user)
            if has_registered:
                return Response({'detail': 'You have previously registered for this event'}, status=400)
            else:
                Attendee.objects.create(event=event, user=user)
                return Response({'detail': 'You have successfully registered for this event'})

        return Response({'detail': 'This Event does not exists'}, status=404)
    
    def get(self, request, *args, **kwargs):
        return Response({'detail': 'Cannot perform get action here.'}, status=400)

    def delete(self, request, *args, **kwargs):
        event_id = self.kwargs.get('id')
        qs = Event.objects.filter(id=event_id)
        if qs.exists():
            event = qs.first()
            user = request.user
            has_registered = Attendee.objects.is_registered(event=event, user=user)
            if has_registered:
                del_count, del_dict = Attendee.objects.get(event=event, user=user).delete()
                if del_count >= 1:
                    return Response({'detail': 'You have successfully unregistered from this event'})
            else:
                return Response({'detail': 'Cant Delete: You havent registered for this event'})

        return Response({'detail': 'This Event does not exists'}, status=404)

    
class EventAttendeesAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserPublicSerializer

    def get_queryset(self):
        event_id = self.kwargs.get('id')
        qs = Event.objects.filter(id=event_id)
        if qs.exists():
            event = qs.first()
            attendees = event.attendees.all()
            if attendees.exists():
                return attendees
    

