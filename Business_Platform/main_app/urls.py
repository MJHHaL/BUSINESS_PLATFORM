from django.urls import path
from . import views


app_name = "url_main"


urlpatterns = [
    
    path("" , views.index , name = "home"),
    path("project/add/" , views.add_projects , name = "add_projects"),
    path("project/update/<project_id>" , views.update_project , name = "update_project"),
    path("project/details/<project_id>" , views.project_details , name = "project_details"),
]