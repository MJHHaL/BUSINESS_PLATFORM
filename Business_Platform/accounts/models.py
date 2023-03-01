from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


class Profile(models.Model):
    
     #choices
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField(default=18 , blank=True , null=True)
    image = models.ImageField(upload_to="images/", default="images/default.jpg" , blank=True , null=True)
    headline = models.CharField(max_length=50 , blank=True , null=True)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100 )
    website = models.CharField(max_length=100 , blank=True , null=True)
    github = models.CharField(max_length=100 , default="github.com" , blank=True , null=True)
    twitter = models.CharField(max_length=100 , default= "twitter.com" , blank=True , null=True)
    bio = models.TextField(max_length=1000 , blank=True , null=True)
    
#     def __str__(self) -> str:
#         return f"{self.user }"
    
def create_profile(sender,**kwargs):
    
    if kwargs['created']:
        user_profile = Profile.objects.create(user = kwargs['instance'])
        
post_save.connect( create_profile , sender = User)


     
class Provider(models.Model):
     
     provider_user = models.ForeignKey(User, on_delete=models.CASCADE)

     def __str__(self) -> str:
      return f"{self.provider_user }"
     
     
class Customers(models.Model):
     
     Customers_user = models.ForeignKey(User, on_delete=models.CASCADE)

     def __str__(self) -> str:
      return f"{self.Customers_user }"