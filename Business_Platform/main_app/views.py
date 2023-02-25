from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Projects , Comments , Section 
from accounts.models import Profile
from customers.models import Orders
from django.contrib.auth.models import User


# Create your views here.


def index(request : HttpRequest):
    projects = Projects.objects.all()
    return render(request , "main/index.html", {"projects" : projects})



def profile(request : HttpRequest , user_id ):
    
    info = Profile.objects.get(user = user_id)
    projects = Projects.objects.filter(user = user_id)
    context = {
        "projects" : projects,
        "info" : info
        
        }
    
    return render(request , "main/profile.html",context)

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
    
#details
def project_details(request : HttpRequest , project_id):
    
    details_project = Projects.objects.get(id = project_id)
    comments = Comments.objects.filter(project_name = details_project)
    
    context = {
        "details_project" :details_project,
        "comments" : comments
    }
    
    return render(request , "main/project_details.html" , context )

def delete_project(request : HttpRequest  , project_id):
    
    project = Projects.objects.get(id=project_id)
    project.delete()
    return redirect("url_main:home")
    
    

def add_Comments(request : HttpRequest, project_id):

    if request.method == "POST":
        project = Projects.objects.get(id=project_id)
        new_review = Comments(
            
            user = request.user,
            project_name=project,
            content = request.POST["content"], 
            # rating = request.POST["rating"]
            )
        new_review.save()

    return redirect("url_main:project_details", project_id=project_id)

# def user_info(request : HttpRequest): 
#     if request.method == "POST":
#         # option = Section.objects.get(id = request.POST["section"])
#         Profile(
#             user = request.user,
#             gender = request.POST["gender"], 
#             age = request.POST["age"], 
#             headline = request.POST["headline"], 
#             phone = request.POST["phone"], 
#             email = request.POST["email"], 
#             website = request.POST["website"], 
#             bio = request.POST["bio"], 
#             image = request.FILES["image"]
#             ).save() 
#         return redirect("url_main:home")
#     return render(request, "main/user_info.html" )

def profile_user(request : HttpRequest):

    return render( request, "main/profile.html")



def orders_received(request : HttpRequest , user_id):
    
    orders = Orders.objects.filter(user = user_id)
  
    return render(request , "main/orders_received.html", {"orders" : orders})



def display_order(request : HttpRequest ):
    orders = Orders.objects.all()
    return render(request , "main/order_manage.html", {"orders" : orders})


