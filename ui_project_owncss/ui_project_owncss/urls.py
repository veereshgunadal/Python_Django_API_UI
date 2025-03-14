"""
URL configuration for ui_project_owncss project.

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
    path('add/', views.add),
    path('addresult/', views.add_result),
    path('get/', views.get),
    path('getresult/', views.get_result),
    path('all/', views.all),
    path('update/', views.update),
    path('updating/', views.updating),
    path('updateresult/<str:name>/', views.update_result),
    path('delete/', views.delete),
    path('deleteresult/<str:name>/', views.delete_result),
    path('notfound/', views.not_found, name="not_found")
]
