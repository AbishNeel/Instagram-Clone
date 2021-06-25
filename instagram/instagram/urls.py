"""instagram URL Configuration

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
from app import views
from . import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('test/', views.test, name="test"),
    path('index.html', views.home, name="home"),
    path('explore/', views.explore, name="explore"),
    path('user_logout/', views.user_logout, name="user_logout"),
    path('profile/', views.profile, name="profile"),
    path('editprofile/', views.editprofile, name="editprofile"),
    path('deletepost/<int:pk>/', views.deletepost, name="deletepost"),
    path('getpostdetails/',views.getpostdetails,name="getpostdetails"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)