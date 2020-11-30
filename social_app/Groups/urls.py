from django.urls import path

from .views import ListGroups, CreateGroup, SingleGroup, JoinGroup, LeaveGroup

app_name = 'social_groups'

urlpatterns = [
    path('', ListGroups.as_view(), name='all_group'),
    path('new/', CreateGroup.as_view(), name='create_group'),
    path('posts/in/<slug>/', SingleGroup.as_view(), name='single_group'),
    path('join/<slug>/', JoinGroup.as_view(), name='join'),
    path('leave/<slug>/', LeaveGroup.as_view(), name='leave'),
]
