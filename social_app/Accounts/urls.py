from django.contrib.auth import views as auth_views
from django.urls import path

from .views import UserCreate

app_name = 'social_accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='socialAccounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', UserCreate.as_view(), name='signup'),
]
