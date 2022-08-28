from rest_framework import viewsets

from . import permissions
from .models import Prosumer
from .serializers import ProsumerSerializer


class ProsumerViewSet(viewsets.ModelViewSet):
    queryset = Prosumer.objects.all()
    serializer_class = ProsumerSerializer
    permission_classes = (permissions.Prosumer,)
