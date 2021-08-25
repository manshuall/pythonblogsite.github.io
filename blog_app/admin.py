from django.contrib import admin
from django.db import models
from .models import Contact_user,Blogs
from django.contrib.auth.models import  User

@admin.register(Contact_user)
class User_commants(admin.ModelAdmin):
    list_display=['id','name','email','subject','comments']

@admin.register(Blogs)
class blog_data(admin.ModelAdmin):
    list_display=['id','title','slug','thambnil','blog_page_img','blog','date','time']



