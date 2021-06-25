from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
    file = models.FileField(upload_to="PostImages/")
    type = models.CharField(max_length=20)
    no_of_likes = models.IntegerField(default=0)
    no_of_comments = models.IntegerField(default=0)
    caption = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return User.username