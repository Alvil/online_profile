from django.urls import path

from .views import CreateWish, WishList
app_name = 'wish'

urlpatterns = [
    path('', WishList.as_view(), name='wishlist'),
    path('create', CreateWish.as_view(), name='create_wish'),
]
