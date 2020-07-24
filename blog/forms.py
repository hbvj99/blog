from django import forms
from . import models


class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'description', 'image']

        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Image'
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter new post title'}),
        }
