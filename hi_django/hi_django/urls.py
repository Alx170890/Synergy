"""hi_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from shortcuts.r import urlsR
# from .GET import urlsG
# from shortcuts.r.get_url import index
from shortcuts.urls import urlpatterns as shortcut_urls
from user.urls import urlpatterns as user_url
import logging

logging.root.setLevel(logging.INFO)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('r/', include(urlsR.urlpatterns)),
    # path('GET/', include(urlsG.urlpatterns)),
    # path('', index),
    path('', include(shortcut_urls)),
    path('user/', include((user_url, 'user'), namespace='u'))
]
