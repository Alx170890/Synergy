from django.contrib import admin

from .models import ShortUrl


class ShortUrlAdmin(admin.ModelAdmin): #для отобрашения в админке django
    pass

admin.site.register(ShortUrl, ShortUrlAdmin)