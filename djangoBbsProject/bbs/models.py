from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='标题')
    content = RichTextField()
    create_at = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='跟帖内容')
    create_at = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
