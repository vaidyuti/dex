from django.contrib import admin

from .models import Prosumer


class ProsumerAdmin(admin.ModelAdmin):
    model = Prosumer


admin.site.register(Prosumer, ProsumerAdmin)
