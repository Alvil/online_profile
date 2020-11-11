from . import views
from django.urls import path

app_name = 'fake'

urlpatterns = [
    path('', views.home, name='home'),
    path('new_user/', views.create_user, name='new_user'),
    path('list', views.UserList.as_view(), name='user-list'),
]
