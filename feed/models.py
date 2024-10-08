from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=31, default="Title")
    text = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[0:100]
