from django.urls import path
from .views import Signup,Signin,home

urlpatterns = [
    path('signup/',Signup, name = "signup"),
    path('signin/',Signin,name = "signin"),
    path('',home,name='home')
]
