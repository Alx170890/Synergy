from django import forms


class AuthForm(forms.Form):
    username = forms.CharField(max_length=256)
    password = forms.CharField(max_length=256, widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=256)
    usersurname = forms.CharField(max_length=256)
    password = forms.CharField(max_length=256, widget=forms.PasswordInput())