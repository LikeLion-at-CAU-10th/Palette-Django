from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(verbose_name="닉네임", max_length=10, default="닉네임", null=True, blank=True)
    category = models.CharField(max_length=100, default="['gray', 'blue', 'green', 'yellow', 'orange', 'red', 'purple']", null=True, blank=True)

    def __str__(self):
        return self.username
