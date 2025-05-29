from django import forms
from .models import BlogPost, BlogComment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']

class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['content'] 