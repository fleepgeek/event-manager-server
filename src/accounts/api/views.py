from django.contrib.auth import authenticate, get_user_model

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

from .permissions import AnonPermissionOnly
from .serializers import UserRegisterSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler    = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

User = get_user_model()

class RegisterAPIView(generics.CreateAPIView):
    permission_classes = [AnonPermissionOnly]
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()


class LoginAPIView(APIView):
    permission_classes = [AnonPermissionOnly]

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({'detail': 'You are already authenticated'}, status=400)
        
        data = request.data   
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            response = jwt_response_payload_handler(token, user, request=request)
            return Response(response)

        return Response({'detail': 'Invalid Credential'}, status=401)
