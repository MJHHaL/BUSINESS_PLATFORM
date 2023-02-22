from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Projects , Comments , Section 

# Create your views here.


def index(request : HttpRequest):
    projects = Projects.objects.all()
    return render(request , "main/index.html", {"projects" : projects})

#to add a new entry
def add_projects(request : HttpRequest):
    
    sections_name  = Section.objects.all()
    if request.method == "POST":
        option = Section.objects.get(id = request.POST["section"])
        Projects(
                user = request.user,
                section = option,
                projects_name= request.POST["projects_name"], 
                description=request.POST["description"],
                image = request.FILES["image"]
                ).save() 
        return redirect("url_main:home")
    return render(request, "main/add_projects.html" , {"sections" : sections_name})

#Update 

def update_project(request : HttpRequest , project_id):
    
    option = Section.objects.all()
    project = Projects.objects.get(id = project_id)
    
    if request.method == "POST":
        choice = Section.objects.get(id = request.POST["section"])
        
        
        project.projects_name = request.POST["projects_name"]
        project.section = choice
        project.description = request.POST["description"]
        project.image = request.FILES["image"]
        project.save()
        return redirect("url_main:home")
    context = {
            "project" : project,
            "options" : option
        }
        
    return render(request , "main/update_project.html" , context)
    
    
def project_details(request : HttpRequest , project_id):
    details_project = Projects.objects.filter(id = project_id)
    
    context = {
        "details_project" :details_project
    }
    
    return render(request , "main/project_details.html" , context )