from rest_framework import serializers

from event.models import Event
from accounts.api.user.serializers import UserPublicSerializer

class EventSerializer(serializers.ModelSerializer):
    creator = UserPublicSerializer(read_only=True)

    class Meta:
        model = Event
        fields = (
            'title', 
            'creator',     
            'category',   
            'tags',       
            'description',
            'event_date', 
            'location',   
            # 'latitude',   
            # 'longitude',  
            'created_on', 
        )

        # read_only_fields = ['user']