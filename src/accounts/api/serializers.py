from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from .permissions import AnonPermissionOnly

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler    = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    token = serializers.SerializerMethodField()
    message = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'token', 'message',)

    def get_token(self, obj):
        user = obj
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token
    
    def get_message(self, obj):
        return 'Registration Successful!'

    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError('Username already taken by another user')
        return value

    def validate_email(self, value):
        qs = User.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError('Email already exists')
        return value

    def validate(self, data):
        pw1 = data.get('password')
        pw2 = data.pop('password2')
        if pw1 != pw2:
            raise serializers.ValidationError('The passwords you entered does not match!')
        return data
    
    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')
        user_obj = User.objects.create(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return user_obj