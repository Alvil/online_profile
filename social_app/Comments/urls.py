from django.urls import path
from .views import (CreateComment,
                    # DeleteComment,
                    )

app_name = 'social_comments'

urlpatterns = [
    path('', CreateComment.as_view(), name='create_comment'),
    # path('<comment_pk>/delete/', DeleteComment.as_view(), name='delete_comment')
]
