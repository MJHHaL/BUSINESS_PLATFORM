from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Orders , User
from accounts.models import Profile
from main_app.models import Projects
from django.contrib.auth.models import User

# Create your views here.


def new_orders(request : HttpRequest , user_id):
    

    sender = Projects.objects.get(id = user_id)
    print("-------------------" , sender)
    if request.method == "POST":
        Orders(
                user = request.user,
                send_to = sender,
                order_name= request.POST["order_name"], 
                content=request.POST["content"],
                ).save() 
        return redirect("url_main:home")
    return render(request, "customer/add_order.html")