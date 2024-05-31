from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    cont = models.TextField()
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)  # New field to store likes

    def __str__(self):
        return self.title