"""
@Project ：djangoBbsProject 
@File    ：urls.py
@Author  ：renjianguo
@Date    ：2023/11/21 16:41 
"""

from django.urls import path

from . import views


urlpatterns = [
    path("register", views.register_view, name='register'),
    path("login", views.login_view, name='login'),
    path("logout", views.logout_view, name='logout'),

    path("post/add", views.post_add_view, name='post_add'),
    path("post/<int:post_id>", views.post_show_view, name='post_show'),
    path("post/<int:post_id>/comment", views.post_comment_view, name='post_comment'),
    # path("post/", views.post_list_view, name='post_list'),

    path('', views.index_view)
]
