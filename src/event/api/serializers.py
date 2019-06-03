from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from event.models import Event, Attendee, Category, Tag
from accounts.api.serializers import UserPublicSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Category
        fields = ('id','name')

class TagSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Tag
        fields = ('id', 'name')

class EventSerializer(serializers.ModelSerializer):
    creator = UserPublicSerializer(read_only=True)
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    uri = serializers.SerializerMethodField()
    class Meta:
        model = Event
        fields = (
            'id',
            'uri',     
            'title', 
            'creator',
            'category',   
            'tags',       
            'description',
            'event_date', 
            'location',   
            # 'latitude',   
            # 'longitude',  
            # 'attendees',
            'created_on',
        )

    def get_uri(self, obj):
        request = self.context.get('request')
        return obj.get_api_uri(request=request)

class EventInlineUserSerializer(EventSerializer):
    class Meta:
        model = Event
        fields = (
            'title', 
            'uri',
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

