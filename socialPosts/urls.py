from django.urls import path, re_path
from . import views

app_name = 'social_posts'

urlpatterns = [
    path('', views.SocialPostList.as_view(), name='all_post'),
    path('new/', views.CreatePost.as_view(), name='create_post'),
    path('by/<username>/', views.UserPosts.as_view(), name='for_user'),
    path('by/<username>/<pk>/', views.PostDetail.as_view(), name='single_post'),
    path('delete/<pk>/', views.DeletePost.as_view(), name='delete_post'),
]
