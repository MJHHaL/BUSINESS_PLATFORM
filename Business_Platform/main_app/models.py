from django.db import models
from django.contrib.auth.models import User
from accounts.models import Customers , Provider





class Section(models.Model):
    section_name = models.CharField(max_length=30)
    
    
    def __str__(self) -> str:
        return f"{self.section_name}"

class Projects(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete= models.CASCADE)
    projects_name = models.CharField(max_length=500)
    description = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/", default="images/default.jpg" , blank= True , null=True)
    like = models.ManyToManyField(User , related_name = "project" ,blank= True , null=True)
    
    def __str__(self) -> str:
        return f"{self.projects_name}"

class Comments(models.Model):

    project_name = models.ForeignKey(Projects, on_delete=models.CASCADE , blank= True , null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank= True , null=True)
    rating = models.FloatField( default="5" , blank= True , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    

    def __str__(self) -> str:
        return f"{self.user}"


class Backlog(models.Model):
    
    customer_user = models.ForeignKey(Customers, on_delete=models.CASCADE , default= 0)
    provider_user = models.ForeignKey(Provider, on_delete=models.CASCADE , default=0)
    order_title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self) -> str:
        return f"{self.customer_user}"
    

class OrderCompleted(models.Model):
    
    customer_user = models.ForeignKey(Customers, on_delete=models.CASCADE)
    provider_user = models.ForeignKey(Provider, on_delete=models.CASCADE)
    order_title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.customer_user}"