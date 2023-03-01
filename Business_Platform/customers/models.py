from django.db import models
from django.contrib.auth.models import User
from accounts.models import Provider

# Create your models here.


class Orders(models.Model):

    order_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    to_provider = models.ForeignKey(Provider , on_delete=models.CASCADE , blank= True , null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self) -> str:
        return f"{self.user } : Send To : {self.to_provider}"



class CommentsOrder(models.Model):

    order_name = models.ForeignKey(Orders, on_delete=models.CASCADE )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length= 1000)
    created_at = models.DateTimeField(auto_now_add=True)