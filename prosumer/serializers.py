from rest_framework import serializers

from .models import Prosumer


class ProsumerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prosumer
        fields = (
            "url",
            "location",
        )
