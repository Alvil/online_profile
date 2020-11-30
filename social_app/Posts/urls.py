from django.urls import path, include
from .views import (SocialPostList, CreatePost, UserPosts,
                    PostDetail, DeletePost)

app_name = 'social_posts'

urlpatterns = [
    path('', SocialPostList.as_view(), name='all_post'),
    path('create/', CreatePost.as_view(), name='create_post'),
    path('by/<username>/', UserPosts.as_view(), name='for_user'),
    path('<pk>/by/<username>/', PostDetail.as_view(), name='single_post'),
    path('<pk>/delete/', DeletePost.as_view(), name='delete_post'),
    path('<pk>/by/<username>/comments/', include('social_app.Comments.urls', namespace='social_comments'),
         name='comment_section'),
]
