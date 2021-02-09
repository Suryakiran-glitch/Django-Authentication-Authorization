from django.urls import path
from .views import users,register,login,logout


urlpatterns = [
    path('users', users),
    path('register',register),
    path('login',login),
    path('logout',logout)
]