from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Orders , User
from accounts.models import Profile
from django.contrib.auth.models import User

# Create your views here.


def new_orders(request : HttpRequest):
    
    if request.method == "POST":
        Orders(
                user = request.user,
                order_name= request.POST["order_name"], 
                content=request.POST["content"],
                ).save() 
        return redirect("url_main:home")
    return render(request, "customer/add_order.html")