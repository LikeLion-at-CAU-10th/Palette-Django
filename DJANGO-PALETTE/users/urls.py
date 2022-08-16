from django.urls import path
from .views import *

urlpatterns = [
    path('', create_user, name="create-user"),
    path('login', user_login, name="user-login"),
    path('logout', user_logout, name="user-logout")
]

