from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    title = models.CharField(max_length=100,blank=True,default='')
    body = models.TextField(blank=True,default='')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title

class Comment(models.Model):
    owner = models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    body = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self) -> str:
        return f"{self.body} | {self.owner}"
        
class Category(models.Model):
    name = models.CharField(max_length=100,blank=False,default='')
    owner = models.ForeignKey(User,related_name='categories',on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='categories',on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name