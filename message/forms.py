from django import forms
from django.forms import ModelForm, Textarea, CharField
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'community_id']
        widgets = {
            'content':Textarea(attrs={'cols':90, 'rows':10})
        }