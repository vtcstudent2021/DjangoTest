"""
@Project ：djangoBbsProject 
@File    ：forms.py
@Author  ：renjianguo
@Date    ：2023/11/21 17:34 
"""
from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']