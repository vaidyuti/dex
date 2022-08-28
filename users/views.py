from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from . import permissions
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        IsAuthenticated,
        permissions.User,
    )
