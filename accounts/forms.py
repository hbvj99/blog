from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

USER = get_user_model()


class CreateUser(UserCreationForm):
    class Meta:
        model = USER
        fields = ['email', 'first_name', 'last_name', 'password1', 'password1']
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Enter your email address i.e. someone@gmail.com'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your surname'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Enter a new password'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Enter again same password as previous'}),
        }


class UserDetail(forms.ModelForm):
    class Meta:
        model = USER
        fields = ['first_name', 'last_name', 'email', 'image']
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Enter new email address i.e. someone@gmail.com'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your new first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your new surname'}),
        }
