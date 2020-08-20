from django.contrib import admin
from django.urls import path
from .views import short_url, long_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', short_url),
    path('<str:short_key>', long_url),
]
