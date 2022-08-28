from rest_framework import viewsets

from . import permissions
from .models import Buy, Sell, Trade
from .serializers import BuySerializer, SellSerializer, TradeSerializer


class BuyViewSet(viewsets.ModelViewSet):
    queryset = Buy.objects.all()
    serializer_class = BuySerializer
    permission_classes = (permissions.Buy,)


class SellViewSet(viewsets.ModelViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer
    permission_classes = (permissions.Sell,)


class TradeViewSet(viewsets.ModelViewSet):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer
    permission_classes = (permissions.Trade,)
