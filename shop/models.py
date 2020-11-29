from django.contrib.auth.models import Group, User
from django.db import models


# Create your models here

class Expert(models.Model):
    user        = models.OneToOneField(to=User,on_delete=models.CASCADE)
    username    = models.CharField(max_length=35)
    first_name  = models.CharField(max_length=35)
    last_name   = models.CharField(max_length=35)
    image       = models.ImageField(upload_to='image expert/', default='image/avatar.png', blank=True, null=True)
    address     = models.CharField(max_length=250)
    phone       = models.CharField(max_length=12)
    email       = models.EmailField(max_length=254)
    category    = models.ManyToManyField(to='Category')
    def __str__(self):
        return self.username

class Customer(models.Model):
    user        = models.OneToOneField(to=User , on_delete=models.CASCADE)
    username    = models.CharField(max_length=35)
    first_name  = models.CharField(max_length=35)
    last_name   = models.CharField(max_length=35)
    phone       = models.CharField(max_length=12)
    email       = models.EmailField(max_length=254)
    def __str__(self):
        return self.username
    
class Tag(models.Model):
    title = models.CharField(max_length=35)
    def __str__(self):
        return self.title
    
class Category(models.Model):
    title   = models.CharField(max_length=35)
    image   = models.ImageField(upload_to='image category/', default='image/default.jpg', blank=True, null=True)
    description = models.CharField(max_length=255 , blank=True , null=True)
    hashtag = models.CharField(max_length=200 , null=True)
    tag     = models.ForeignKey(to=Tag,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
class Request_srv(models.Model):
    title       = models.CharField(max_length=35)
    phone       = models.CharField(max_length=12)
    address     = models.CharField(max_length=100)
    category    = models.ForeignKey(to=Category,on_delete=models.CASCADE)
    description = models.CharField(max_length=300,blank=True,null=True)
    expert      = models.ForeignKey(to=Expert,on_delete=models.CASCADE)
    customer    = models.ForeignKey(to=Customer,on_delete=models.CASCADE)
    update_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
