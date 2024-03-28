from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as login_action, logout as logout_action
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm, CommentForm


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = UserCreationForm()
    return render(request, 'bbs/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login_action(request, user)
                # 登录成功后重定向到首页或其他需要的页面
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'bbs/login.html', {'form': form})


def logout_view(request):
    logout_action(request)
    return redirect('/login')


@login_required
def post_add_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post_obj = form.save(commit=False)
            post_obj.user = request.user
            post_obj.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'bbs/create.html', {'form': form})


def post_show_view(request, post_id):
    obj = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    return render(request, "bbs/show.html", {"post": obj, 'comment_form': comment_form})


@login_required
def post_comment_view(request, post_id):
    if request.method == 'POST':
        post_obj = get_object_or_404(Post, pk=post_id)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_obj = comment_form.save(commit=False)
            comment_obj.user = request.user
            comment_obj.post = post_obj
            comment_obj.save()
            return redirect('post_show', post_id)


def index_view(request):
    page = Paginator(Post.objects.order_by('-id').all(), 10).get_page(request.GET.get('page'))
    return render(request, 'bbs/index.html', {'page': page})
