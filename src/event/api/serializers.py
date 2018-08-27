from rest_framework import serializers

from event.models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            # 'creator',    
            'title',      
            'category',   
            'tags',       
            'description',
            'event_date', 
            'location',   
            # 'latitude',   
            # 'longitude',  
            'created_on', 
        )