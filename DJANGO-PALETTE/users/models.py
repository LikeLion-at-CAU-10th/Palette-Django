from django.db import models

# Create your models here.
class User(models.Model):
    userId = models.CharField(verbose_name="사용자ID", max_length=15)
    nickname = models.CharField(verbose_name="닉네임", max_length=10)
    password = models.CharField(verbose_name="사용자비밀번호", max_length=15)

    def __str__(self):
        return self.userId
