"""
URL configuration for ui_projectv1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('getmovie/', views.get_movie),
    path('getmovie_result/', views.get_movie_result),
    path('addmovie/', views.add_movie),
    path('addmovie_result/', views.add_movie_result),
    path('updatemovie/', views.update_movie),
    path('updatemovie_result/', views.update_movie_result),
    path('deletemovie/', views.delete_movie),
    path('deletemovie_result/', views.delete_movie_result),
]
