from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Orders , User
from accounts.models import Profile
from main_app.models import Projects
from django.contrib.auth.models import User

# Create your views here.


#list
def order_list(request : HttpRequest , user_id):
    
    orders = Orders.objects.filter(user = user_id)
  
    return render(request , "customer/customer_panel.html", {"orders" : orders})


def new_orders(request : HttpRequest , user_id):
    
    sender = Projects.objects.get(id = user_id)
    if request.method == "POST":
        Orders(
                user = request.user,
                send_to = sender,
                order_name= request.POST["order_name"], 
                content=request.POST["content"],
                ).save() 
        return redirect("url_customers:order_list")
    return render(request, "customer/add_order.html")


def new_public_orders(request : HttpRequest , order_id):
    
    sender = User.objects.get(id = order_id)
    if request.method == "POST":
        Orders(
                user = request.user,
                send_to = sender,
                order_name= request.POST["order_name"], 
                content=request.POST["content"],
                ).save() 
        return redirect("url_main:home")
    return render(request, "customer/add_order.html")


def update_order(request : HttpRequest , order_id):
    
    order = Orders.objects.get(id = order_id)
    
    if request.method == "POST":
        
        order.user = request.user
        order.order_name = request.POST["order_name"]
        order.send_to = request.POST["send_to"]
        order.content = request.POST["content"]
        order.save()
        return redirect("url_customers:update_order")
    context = {
            "order" : order,
            
        }
        
    return render(request , "customer/update_order.html" , context)
    
    
def delete_order(request : HttpRequest  , order_id):
    
    order = Orders.objects.get(id=order_id)
    order.delete()
    return redirect("url_main:home")