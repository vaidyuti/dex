from django.contrib import admin

from .models import Buy, Sell, Trade


class BuyAdmin(admin.ModelAdmin):
    model = Buy


class SellAdmin(admin.ModelAdmin):
    model = Sell


class TradeAdmin(admin.ModelAdmin):
    model = Trade


admin.site.register(Buy, BuyAdmin)
admin.site.register(Sell, SellAdmin)
admin.site.register(Trade, TradeAdmin)
