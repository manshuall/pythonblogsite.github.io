"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from blog_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page),
    path('about',views.about),
    path('contact',views.contact),
    path('blog',views.blog),
    path('marketing',views.marketing),
    path('login',views.login),
    path('register',views.register),
    path('User_login',views.User_login),
    path('logout',views.user_logout),
    path('Contact_data',views.contact_data_save),
    path('post/<str:slug>',views.post),
    path('read',views.read),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
