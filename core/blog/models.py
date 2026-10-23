from django.db import models
from accounts.models import User
# Create your models here
class Post (models.Model):
    image = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length=150)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey("Category",on_delete=models.SET_NULL,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    pubished_date = models.DateTimeField()


    def __str__(self):
        return self.title

class Category (models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name