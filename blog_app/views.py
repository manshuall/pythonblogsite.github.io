from django.contrib import auth
from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Contact_user,Blogs
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import sessions
from django.contrib.auth import login as Login_data

# all html page in nav bar

def home_page(req):
    data=Blogs.objects.filter().order_by('id').reverse()[0:3]
    return render(req,"site_html/index.html",{"blog_data":data})

def about(req):
    return render(req,"site_html/about.html")

def contact(req):
    return render(req,"site_html/contact.html")
def contact_data_save(req):
    if req.method=="POST":
        name=req.POST.get("name")
        email=req.POST.get("email")
        subject=req.POST.get("subject")
        Comment=req.POST.get("Comment")
        data=Contact_user(name=name,email=email,comments=Comment,subject=subject)
        data.save()
        messages.success(req,"Thenkyou For Your value full Feedback")
        return render(req,"site_html/index.html")

def blog(req):
    data=Blogs.objects.all().order_by('id').reverse()
    return render(req,"site_html/blog.html",{"blog_data":data})

def marketing(req):
    return render(req,"site_html/marketing.html")

def login(req):
    return render(req,"site_html/login_form.html")

def register(req):
    if req.method=="POST":
        name=req.POST.get("user_name")
        email=req.POST.get("user_email")
        password=req.POST.get("user_pass")
        if User.objects.filter(username=email).exists():
            messages.error(req,"user alredy exist")
            return render(req,"site_html/index.html")
        else:
            user=User.objects.create_user(username=email,first_name=name,password=password)
            user.save()
            messages.success(req,"success")
            return render(req,"site_html/index.html")
        
def User_login(req):
    if req.method=="POST":
        user_name=req.POST['email']
        user_pass=req.POST['password']
        auth_user=authenticate(username=user_name,password=user_pass)
        
        logind=Login_data(req,auth_user)  
        print(logind) 
        return HttpResponseRedirect("http://127.0.0.1:8000/",{"user":auth_user}) 
        # return render(req,"site_html/index.html",{"user":auth_user})   


def post(req,slug):
    post_data=Blogs.objects.filter(slug=slug)
    return render(req,"site_html/read.html",{"data":post_data})

def read(req):
    return render(req,"site_html/read.html")
   
def user_logout(req):
    logout(req)
    return HttpResponseRedirect("http://127.0.0.1:8000/")