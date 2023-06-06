"""
URL configuration for crm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from .views import Home, Company, CreateCompany, CreateUser, Login, Main, Users
app_name = 'core'
urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('company', Company.as_view(), name='company'),
    path('create-company/', CreateCompany.as_view(), name='create_company'),
    path('create-user/', CreateUser.as_view(), name='create_user'),
    path('login/', Login.as_view(), name='login'),
    
    path('users/', Users.as_view(), name='users'),
]
