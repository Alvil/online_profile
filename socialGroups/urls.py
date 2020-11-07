from django.urls import path, re_path
from . import views

app_name = 'social_groups'

urlpatterns = [
    path('', views.ListGroups.as_view(), name='all_group'),
    path('new/', views.CreateGroup.as_view(), name='create_group'),
    path('posts/in/<slug>/', views.SingleGroup.as_view(), name='single_group'),
    path('join/<slug>/', views.JoinGroup.as_view(), name='join'),
    path('leave/<slug>/', views.LeaveGroup.as_view(), name='leave'),
]
