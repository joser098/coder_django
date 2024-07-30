from django import forms
from .models import Post, Autores

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']\

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autores
        fields = ['name', 'email', 'posts']
