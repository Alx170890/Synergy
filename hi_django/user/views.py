from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
import logging
from .auth_form import AuthForm
from django.contrib.auth import authenticate, login
from django import shortcuts
from django.contrib.auth.models import User

def auth(request: HttpRequest):
    if request.method != "POST":
        return HttpResponse("Failed request", status=405)

    form = AuthForm(request.POST)
    if not form.is_valid():
        # return HttpResponse("Invalid form data", status=405)# если пароль не верный повторить вывод формы и запрос пароля
        return HttpResponseRedirect(request.GET['redirect'])
    user = authenticate(request=request, **form.cleaned_data)
    # print(user)
    if not user:
        # return HttpResponse("User is not registered", status=404)
        # return HttpResponseRedirect(request.GET['redirect'])
        return HttpResponseRedirect('/register')

    login(request, user=user)
    # print(login)
    # logging.info("Auth from %r", request.user)

    return HttpResponseRedirect(request.GET['redirect'])

def register(request: HttpRequest):
    return shortcuts.render(request, 'register.html')

def create_user(request: HttpRequest):
    if request.method == "POST":
        user = User.objects.create_user('myugfhdername', 'mypassdwgfhbord')