from django.contrib import admin
from django.urls import path
from .redirect import short_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', short_url),
]
