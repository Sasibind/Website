from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=31)
    text = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title[0:100]
