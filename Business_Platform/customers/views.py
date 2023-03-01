from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Orders , User , Provider  , CommentsOrder
from accounts.models import Profile , Customers 
from main_app.models import Projects , Backlog , Comments
from django.contrib.auth.models import User

# Create your views here.

def orders_public(request : HttpRequest ):
    """Function to view all public orders"""
    
    orders = Orders.objects.all().order_by("-id")
    context = {
        "orders" : orders
    } 
    return render(request , "customer/order_list.html" , context)
    
def order_public_details(request : HttpRequest , order_id):
    """Function to display details order by id"""
    comments = CommentsOrder.objects.filter(order_name = order_id)
    order = Orders.objects.get(id = order_id)
    order_user = Profile.objects.get(user = order.user)
    return render(request , "customer/orders_public.html" ,  {"orders" : order , "order_user" : order_user , "comments" : comments})


def order_list(request : HttpRequest , user_id):
    """Function to display all orders of the user customer"""
    if not request.user.id == int(user_id) :
        return render(request, "main/no_permission.html")
    orders = Orders.objects.filter(user = user_id)
    order_user = Customers.objects.get(Customers_user =  request.user.id)
    order_accepted = Backlog.objects.filter(customer_user = order_user)
    print("----------------------------------" ,order_accepted)
    
    context = {"order_accepted" : order_accepted , "orders" : orders}
    return render(request , "customer/customer_panel.html", context)


def new_orders(request : HttpRequest , user_id):
    """function allows to create by special order to provider"""
    # if not request.user.id == int(user_id):
    #     return render(request, "main/no_permission.html")
    project_user = User.objects.get(id = user_id)
    provider = Provider.objects.get(provider_user = project_user)
    if request.method == "POST":
        Orders(
                user = request.user,
                to_provider = provider,
                order_name= request.POST["order_name"], 
                content=request.POST["content"],
                ).save() 
        return redirect("url_customers:orders_public")
    return render(request, "customer/add_order.html")


def new_public_orders(request : HttpRequest , order_id):
    """function allows to create by public order to all"""
    sender = User.objects.get(id = order_id)
    if request.method == "POST":
        Orders(
                user = request.user,
                order_name= request.POST["order_name"], 
                content=request.POST["content"],
                ).save() 
        return redirect("url_main:home")
    return render(request, "customer/add_order.html")


def update_order(request : HttpRequest , order_id):
    """function allows to update order details"""
    order = Orders.objects.get(id = order_id)
    
    if request.method == "POST":
        
        order.user = request.user
        order.order_name = request.POST["order_name"]
        order.content = request.POST["content"]
        order.save()
        return redirect("url_customers:update_order")
    context = {
            "order" : order,
            
        }
        
    return render(request , "customer/update_order.html" , context)
    
    
def delete_order(request : HttpRequest  , order_id):
    """function  to to delete special order"""
    order = Orders.objects.get(id=order_id)
    order.delete()

    return redirect("url_customers:order_list", user_id=request.user.id)


def add_public_comments(request : HttpRequest, order_id):
    """function allows to all users create comment for public orders"""
    if request.method == "POST":
       
        order = Orders.objects.get(id=order_id)
        new_comment = CommentsOrder(
            user = request.user,
            order_name = order,
            content = request.POST["content"], 
            )
        new_comment.save()

    return redirect("url_customers:order_public_details" , order_id =order_id )



def delete_order_comment(request : HttpRequest  , comment_id , order_id):
    """ to delete comments -customer model-"""
    comment = CommentsOrder.objects.get(id=comment_id)
    comment.delete()
    return redirect("url_customers:order_public_details" , order_id = order_id )