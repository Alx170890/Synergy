# from django.contrib import admin
from django.urls import path, include
from shortcuts.views import index
from .r import urlsR
from user.views import register

urlpatterns = [
    path('', index),
    path('r/', include(urlsR.urlpatterns)),
    path('register/', register)
]
