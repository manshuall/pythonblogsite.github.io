from datetime import datetime
from django.db import models
from django.db.models.fields import CharField, DateField, TimeField
from django.utils import timezone
class Contact_user(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=200,default="No subject")
    comments=models.TextField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'blog_app_contact_user'
        # Add verbose name
        verbose_name = 'User commants Detail'

class Blogs(models.Model):
    title=models.CharField(max_length=400)
    slug=models.CharField(max_length=50)
    thambnil=models.ImageField(upload_to="images")
    blog_page_img=models.ImageField(upload_to="images",default="images/blog_1.png")
    blog=models.TextField()
    date=models.DateField(default=datetime.now)
    time=models.TimeField(default=timezone.now)
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'blog_app_blogs'
        # Add verbose name
        verbose_name = 'Blog'
