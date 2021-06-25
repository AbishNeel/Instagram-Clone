from .models import *
from post.models import *
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/")
def explore(request):
    #Post.objects.all().delete()
    all_posts = Post.objects.all().order_by("-pk")
    if request.method == "POST":
        caption = request.POST.get('caption')
        file = request.FILES.get('file')
        type = str(file).split(".")[-1]
        types= ["png","jpg","jpeg","jfif"]
        if type in types:
            type = "image"
        else:
            type = "video"
        user_obj = UserInfo.objects.get(user=request.user)
        user_obj
        obj = Post.objects.create(caption=caption, file=file, type=type, user=request.user)    
        return redirect("/")
    return render(request, 'home.html', {'all_posts':all_posts})