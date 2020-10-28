from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.logIn, name='login' ),
    path('signUp/', views.signUp, name='signUp'),
    path('logout/', views.logOut, name='logout'),
    path('profile/', views.profile, name='profile')
]