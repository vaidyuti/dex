from rest_framework import serializers

from .models import Buy, Sell, Trade


class BuySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Buy
        fields = (
            "url",
            "buyer",
            "opening_time",
            "closing_time",
            "units",
            "status",
        )


class SellSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sell
        fields = (
            "url",
            "seller",
            "opening_time",
            "closing_time",
            "units",
            "unit_price",
            "status",
        )


class TradeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trade
        fields = (
            "url",
            "buy",
            "sell",
            "opening_time",
            "closing_time",
            "units",
            "unit_price",
        )
