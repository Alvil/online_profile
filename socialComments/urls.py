from django.urls import path
from . import views

app_name = 'social_comments'

urlpatterns = [
    path('', views.CreateComment.as_view(), name='create_comment'),
    path('delete/<comment_pk>', views.DeleteComment.as_view(), name='delete_comment')
]
