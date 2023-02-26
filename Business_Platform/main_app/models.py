from django.db import models
from django.contrib.auth.models import User





class Section(models.Model):
    section_name = models.CharField(max_length=30)
    
    
    def __str__(self) -> str:
        return f"{self.section_name}"

class Projects(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete= models.CASCADE)
    projects_name = models.CharField(max_length=500)
    description = models.TextField()
    rating = models.FloatField( default="5")
    created_at  = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    
    def __str__(self) -> str:
        return f"{self.projects_name}"

class Comments(models.Model):

    project_name = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self) -> str:
        return f"{self.user}"


# class Backlog(models.Model):
    
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     order_name = models.CharField(max_length=100)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
    

#     def __str__(self) -> str:
#         return f"{self.user}"
    