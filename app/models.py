from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/',null=True)
    date_created = models.DateTimeField(auto_now=True)
    

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='profile/',null=True)
    # posts = models.ForeignKey(Post)
    