from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
    phone_number = models.BigIntegerField()
    no_of_posts = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    bio = models.CharField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.User.username