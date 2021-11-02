from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

class BlogPost(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)
    tag=models.CharField(max_length=50)
    thumbnail=models.ImageField(upload_to='blog/')
    desc=models.CharField(max_length=500)
    content=models.TextField()
    pub_date=models.DateField(auto_now_add=True)
    pub_time=models.TimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering=['-pub_date', '-pub_time']

class Comment(models.Model):
    sno=models.AutoField(primary_key=True)
    commenter=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment=models.CharField(max_length=1000)
    post_date=models.DateField(auto_now_add=True)
    post_time=models.TimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.comment
    
    class Meta:
        ordering=['-post_date', '-post_time']
