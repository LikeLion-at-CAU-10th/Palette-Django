from django.db import models

# Create your models here.
class Post(models.Model):
    CHOICES = (
        ("01", "gray"),
        ("02", "blue"),
        ("03", "green"),
        ("04", "yellow"),
        ("05", "orange"),
        ("06", "red"),
        ("07", "pink"),
    )

    category = models.CharField(max_length=10, choices=CHOICES)
    writer = models.CharField(verbose_name="작성자", max_length=10)
    color = models.CharField(verbose_name="본문색상", max_length=7)
    title = models.CharField(verbose_name="제목", max_length=20)
    content = models.TextField(verbose_name="내용")
    pup_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title