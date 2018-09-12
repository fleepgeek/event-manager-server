from django.contrib.auth import get_user_model
from rest_framework import serializers

from event.api.serializers import EventInlineUserSerializer
from event.models import Attendee
User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'display_name', 'about',)

