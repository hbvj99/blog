from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

USER = get_user_model()


class CreateUser(UserCreationForm):
    class Meta:
        model = USER
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']


class UserDetail(forms.ModelForm):
    class Meta:
        model = USER
        fields = ['first_name', 'last_name', 'email', 'image']
