from django import forms
from . import models


class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'description', 'author', 'image']

        labels = {
            'title': 'Title',
            'description': 'Description',
            'Author': 'Author',
            'image': 'Image'
        }