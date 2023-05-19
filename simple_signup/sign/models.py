from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label='email')
    first_name = forms.CharField(max_length=64, label='Name')
    last_name = forms.CharField(max_length=64, label='Surname')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
