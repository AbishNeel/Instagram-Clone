from post.models import *
from .models import *
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect("/explore/")
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("/explore/")
    return render(request, 'index.html',)

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        bio = request.POST.get('bio')
        print(username)
        user_obj = User.objects.create(username=username,first_name = name, email=email)
        user_obj.set_password(password)
        user_obj.save()
        user_info_obj = UserInfo.objects.create(phone_number=phone, bio=bio, user=user_obj)
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/explore/')
    return render(request, 'signup.html',)

def user_logout(request):
    logout(request)
    return redirect("/")

def test(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        obj= User.objects.create(username=username, email=email)
        obj.set_password(password)
        obj.save()
    return render(request, 'test.html',)

def profile(request):
    user_info_obj = UserInfo.objects.get(user = request.user)
    posts = Post.objects.filter(user=request.user).order_by("-pk")
    context = {'user_info_obj':user_info_obj, 'posts':posts,}
    return render(request, 'profile.html', {'context':context})

def editprofile(request):
    print("inside editprofile")
    user_info_obj = UserInfo.objects.get(user = request.user)
    posts = Post.objects.filter(user=request.user).order_by("-pk")
    if request.method == "POST":
        username = request.POST.get("username")
        name = request.POST.get("name")
        user_obj = request.user
        user_obj.first_name = name
        user_obj.save()
        bio = request.POST.get("bio")
        user_info_obj.bio = bio
        user_info_obj.save()
        try:
            user_obj = User.objects.get(username = username)
            return redirect("/editprofile/")
        except Exception as e:
            user_obj = request.user
            user_obj.username = username
            user_obj.save()

            return redirect('/profile/')
        pass
    context = {
        'user_info_obj':user_info_obj,
        'posts':posts,
    }
    return render(request,'editprofile.html', {'context':context})

def deletepost(request,pk):
    post = Post.objects.get(pk=int(pk))
    post.delete()
    user_info_obj = UserInfo.objects.get(user=request.user)
    user_info_obj.no_of_posts = user_info_obj.no_of_posts - 1
    user_info_obj.save()
    return redirect('/editprofile/')

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
        user_info_obj = UserInfo.objects.get(user=request.user)
        user_info_obj.no_of_posts = user_info_obj.no_of_posts +1
        user_info_obj.save()
        obj = Post.objects.create(caption=caption, file=file, type=type, user=request.user)    
        return redirect("/")
    return render(request, 'home.html', {'all_posts':all_posts})

def getpostdetails(request):
    postid = request.GET.get('postid')
    print(postid)
    post = Post.objects.get(pk=postid)
    l=[]

    l.append(str(post.file))
    l.append(post.user.username)
    l.append(post.caption)
    return JsonResponse(l,safe=False)    