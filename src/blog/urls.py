from django.urls import path
from blog.views import BlogHome, BlogPostCreate, BlogPostUpdate, BlogPostDetail, BlogPostDelete
from django.contrib.auth.decorators import login_required

app_name = "blog"

urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('create/', login_required(BlogPostCreate.as_view()), name='create'),
    path('<str:slug>/', BlogPostDetail.as_view(), name='post'),
    path('edit/<str:slug>', login_required(BlogPostUpdate.as_view()), name='edit'),
    path('delete/<str:slug>', login_required(BlogPostDelete.as_view()), name='delete'),
]
