from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Reducer


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget= forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget= forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget= forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор Пароля', widget= forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ReducerForm(forms.ModelForm):
    origin_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Your URL to shorten"}))

    class Meta:
        model = Reducer
        fields = ('origin_url', )