from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 250)
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) #useful for 'last-modified' stamps
    photo = models.ImageField()

    def __str__(self):
        return self.title
