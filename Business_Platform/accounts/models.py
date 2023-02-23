from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


class Profile(models.Model):
    
     #choices
    gender_choices = models.TextChoices("Gender", ["male", "female"])
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField(default=18)
    gender = models.CharField(max_length=64, choices=gender_choices.choices)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    headline = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000)
    
    def __str__(self) -> str:
        return f"{self.user }"
    
def create_profile(sender,**kwargs):
    
    if kwargs['created']:
        user_profile = Profile.objects.create(user = kwargs['instance'])
        
post_save.connect( create_profile , sender = User)