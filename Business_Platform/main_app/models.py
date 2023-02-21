from django.db import models
from django.contrib.auth.models import User



class Section(models.Model):
    section_name = models.CharField(max_length=30)
    

class Projects(models.Model):
    
    projects_name = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    rating =  models.FloatField()
    date_at  = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f"{self.projects_name}"

class Comments(models.Model):

    project_name = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


