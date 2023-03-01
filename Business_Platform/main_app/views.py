from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Projects , Comments , Section , Backlog , OrderCompleted
from accounts.models import Profile , Provider , Customers 
from customers.models import Orders
from django.contrib.auth.models import User


# Create your views here.


def index(request : HttpRequest ):
    """Function to view all projects in index page"""
    
    projects = Projects.objects.all()
    return render(request , "main/index.html", {"projects":projects})





def provider_panel(request : HttpRequest , user_id ):
    """function display to provider manage all projects and orders  """
    if not request.user.id == int(user_id) or not request.user.has_perm("main_app.view_projects"):
        return render(request, "main/no_permission.html")
       
    info = Profile.objects.get(user = user_id)
    projects = Projects.objects.filter(user = user_id)
    
    #to count orders 
    provider = Provider.objects.get(provider_user = user_id)
    count_orders = Orders.objects.filter(to_provider = provider).count()
    count_orders_accepted = Backlog.objects.filter(provider_user = provider).count()
    count_orders_complected = OrderCompleted.objects.filter(provider_user = provider).count()
    context = {
        "projects" : projects,
        "info" : info,
        "count_orders" : count_orders,
        "count_orders_accepted" : count_orders_accepted,
        "count_orders_complected" : count_orders_complected
        
        }
    
    return render(request , "main/provider_panel.html",context)

#to add a new entry
def add_projects(request : HttpRequest):
    """function allows to create new projects for provider"""
    if not request.user.has_perm("main_app.view_projects"):
        return render(request, "main/no_permission.html")
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
    """function  to update projects details to provider"""
    if not request.user.has_perm("main_app.view_projects"):
        return render(request, "main/no_permission.html")
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
    """function to display details of projects"""
    
    details_project = Projects.objects.get(id = project_id)
    project_user = User.objects.get(username = details_project.user )
    comments = Comments.objects.filter(project_name = project_id)
    # user_like = User.objects.get(id = request.user.id)
    img = Profile.objects.get(user = details_project.user)
    
    context = {
        "details_project" :details_project,
        "comments" : comments,
        "img" : img
    }
    
    return render(request , "main/project_details.html" , context)
     
    

def delete_project(request : HttpRequest  , project_id):
    """function allows to delete one project to provider"""
    project = Projects.objects.get(id=project_id)
    project.delete()
    return redirect("url_main:home")
    
# def most_comment(request : HttpRequest):
#     """"""
    
#     most_rate = Projects.objects.all().order_by("-comments")
#     context ={
#         "most_comment" : most_rate,
#     }
#     return render(request , "main/most_comment.html", context)

def add_Comments(request : HttpRequest, project_id):
    """function allows to add comment for specific projects"""
    if request.method == "GET":

        project = Projects.objects.get(id=project_id)
        new_review = Comments(
            
            user = request.user,
            project_name=project,
            content = request.GET["content"], 
            rating = request.GET["rating"]
            )
        new_review.save()

    return redirect("url_main:project_details", project_id=project_id)



def profile_user(request : HttpRequest):
    """function  to navigation to  profile page"""
    return render( request, "main/provider_panel.html")


def orders_details(request : HttpRequest , order_id):
    """function  to display details of special orders"""
    order = Orders.objects.get(id = order_id)
    order_user = Profile.objects.get(user = order.user )

    return render(request , "main/order_detils.html" , {"order_details" : order , "order_user" : order_user})


    
def orders_received(request : HttpRequest , user_id):
    """function  to display all of orders received to provider"""
    if not request.user.id == int(user_id):
        return render(request, "main/no_permission.html")
    provider = Provider.objects.get(provider_user = user_id)
    orders = Orders.objects.filter(to_provider = provider).order_by("-id")
    
    return render(request , "main/orders_received.html", {"orders" : orders})



# def display_order(request : HttpRequest ):
#     orders = Orders.objects.all()
#     return render(request , "main/order_manage.html", {"orders" : orders})


def delete_comment(request : HttpRequest  , comment_id , project_id):
    """function  to delete comment -projects-"""
    comment = Comments.objects.get(id=comment_id)
    comment.delete()
    return redirect("url_main:project_details" , project_id = project_id )
    
    
def order_by_section(request : HttpRequest  , section_num):
    """function  to display projects by category"""
    projects_by_section = Projects.objects.filter(section = section_num )
    context = {
        "projects_section" : projects_by_section ,
         }
    return render(request , "main/section.html", context)


def orders_accepted(request : HttpRequest , order_id):
    """Function to accept orders for provider"""
    msg = None
    order = Orders.objects.get(id = order_id)
    user = User.objects.get(username = order.to_provider)
    provider = Provider.objects.get(provider_user = user)
    order_user = Customers.objects.get(Customers_user = order.user)
    Backlog(
        customer_user = order_user,
        provider_user = provider,
        order_title = order.order_name , 
        content = order.content  ,
        created_at = order.created_at
        ).save() 
    msg= "Accepted"
   
    return render(request , "main/orders_received.html" , {"msg" : msg})

def orders_completed(request : HttpRequest , order_id):
    
    """Function  to create completed orders for provider"""
    msg = None
    order = Backlog.objects.get(id = order_id)
    user = User.objects.get(username = order.provider_user)
    user2 = User.objects.get(username = order.customer_user)
    provider = Provider.objects.get(provider_user = user)
    order_user = Customers.objects.get(Customers_user = user2)
    OrderCompleted(
        customer_user = order_user,
        provider_user = provider,
        order_title = order.order_title , 
        content = order.content  ,
        created_at = order.created_at
        ).save() 
    msg= "completed"
    print("-----------------------"  , order.delete())
    return render(request , "main/orders_received.html" , {"msg" : msg})


def orders_done(request : HttpRequest , user_id):
    """Function  to display completed orders for provider"""
    provider_user = Provider.objects.get(provider_user = request.user)
    # customer_user = Customers.objects.get(provider_user = request.user)
    orders = OrderCompleted.objects.filter(provider_user = provider_user).order_by("-id")
    
    context = {
        "orders" : orders
    }
    return render(request , "main/orders_complated.html" , context)



def orders_progress(request : HttpRequest):
    """Function  to display pending orders for provider"""
    user = Provider.objects.get(provider_user = request.user)
    orders = Backlog.objects.filter(provider_user = user ).order_by("-id")
    context = {
        "orders" : orders
    }
    return render(request , "main/progress.html" , context)


def user_favorites(request : HttpRequest ,  project_id ):
    """function that allows users to give likes to project"""
    details_project = Projects.objects.get(id = project_id)
    user_like = User.objects.get(id = request.user.id)
   
    if user_like in details_project.like.all():
        details_project.like.remove(user_like)
        return redirect("url_main:project_details" , project_id = details_project.pk )
    else:
        details_project.like.add(user_like)
        return redirect("url_main:project_details" , project_id = details_project.pk )
    
    
def projects_liked(request : HttpRequest ,  user_id ):
    """ function to display favorites projects """
    user_like = Projects.objects.filter(like = user_id)
    
   
    return render(request , "main/favorite.html" , {"user_like" : user_like})
    