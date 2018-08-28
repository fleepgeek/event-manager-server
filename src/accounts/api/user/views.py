from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from .serializers import UserDetailSerializer

User = get_user_model()

class UserEventAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    lookup_field = 'username'