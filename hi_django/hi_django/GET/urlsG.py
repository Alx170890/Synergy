from django.contrib import admin
from django.urls import path
from .get_url import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]
