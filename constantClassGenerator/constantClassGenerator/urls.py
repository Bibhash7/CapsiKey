"""
URL configuration for constantClassApp project.

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
from django.urls import path, re_path
from constantClassApp import views
from .settings import DEBUG

if DEBUG:
    urlpatterns = [
        path("admin/", admin.site.urls),
        path("", views.home, name='home'),
        path('sign-in/', views.sign_in, name='sign_in'),
        path('sign-up/', views.sign_up, name='sign_up'),
        path('constant-class_create/', views.constant_class_create, name='constant_create'),
        path('sign-out/',views.sign_out, name = 'sign_out'),
        path('get-user-count/', views.get_user_count, name='get_user_count'),
        re_path(r'^.*$', views.handle_unknown_routes),
    ]
else:
    urlpatterns = [
        path("", views.home, name='home'),
        path('sign-in/', views.sign_in, name='sign_in'),
        path('sign-up/', views.sign_up, name='sign_up'),
        path('constant-class-create/', views.constant_class_create, name='constant_create'),
        path('sign-out/', views.sign_out, name='sign_out'),
        path('get-user-count/', views.get_user_count, name='get_user_count'),
        re_path(r'^.*$', views.handle_unknown_routes),
    ]
