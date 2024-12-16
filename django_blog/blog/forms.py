from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment
from taggit.forms import TagWidget
from django.forms import widgets

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

   # Example of using a standard widget from django.forms
    title = forms.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title here'}),
        required=True
    )
    content = forms.CharField(
        widget=widgets.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter post content here'}),
        required=True
    )
    
    # Example of using the TagWidget from django-taggit
    tags = forms.CharField(
        widget=TagWidget(),  # TagWidget from django-taggit to handle input
        required=False  # Tags are optional
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Write a comment...'})

