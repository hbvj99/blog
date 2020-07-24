from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

USER = get_user_model()


class CreateUser(UserCreationForm):
    class Meta:
        model = USER
        fields = ['email', 'password1', 'password2']
