from django.contrib.auth import get_user_model
from rest_framework import serializers

from event.api.serializers import EventInlineUserSerializer

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    events = serializers.SerializerMethodField()
    # events = EventInlineUserSerializer(source='event_set', many=True, read_only=True)
    class Meta:
        model = User
        fields = ('username', 'events',)
    
    def get_events(self, obj):
        qs = obj.event_set.all().order_by('-created_on')
        data = EventInlineUserSerializer(qs, many=True).data
        return data