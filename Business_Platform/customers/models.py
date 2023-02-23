from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Orders(models.Model):

    order_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self) -> str:
        return f"{self.user}"

