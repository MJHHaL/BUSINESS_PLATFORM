from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User ,Group
from django.contrib.auth import authenticate, login, logout
from .models import Profile , Provider , Customers

# Create your views here.
def register_user(request : HttpRequest):
    # if User.objects.filter(User.username == request.POST["username"]).first():
    #     msg = "xxxx"
    
    msg = None
    if request.method == "POST":
        user_choice = int(request.POST["type_user"])
        print("---------------------" , user_choice ," ", type(user_choice))
        if user_choice == 1:
            new_user = User.objects.create_user(
            username=request.POST["username"], 
            email=request.POST["email"],
            password=request.POST["password"],
            first_name = request.POST["first_name"],
            last_name = request.POST["last_name"] ,     
        )
            new_user.save()
            group = Group.objects.get(name='customers')
            new_user.groups.add(group)
            Customers(Customers_user = new_user).save()
            return redirect("url_accounts:login_user")
            
        elif  user_choice  == 2:
            new_user = User.objects.create_user(
            username=request.POST["username"], 
            email=request.POST["email"],
            password=request.POST["password"],
            first_name = request.POST["first_name"],
            last_name = request.POST["last_name"] ,     
        )
            new_user.save()
            group = Group.objects.get(name='providers')
            new_user.groups.add(group)
            Provider(provider_user = new_user).save()
            return redirect("url_accounts:login_user")    
        else:
            msg = "please Choice type user !"
            
    return render(request, "accounts/register.html" , {"msg" : msg} )


def login_user(request : HttpRequest):

    loggin_msg = None
    if request.method == "POST":
        #authenticate user credentials
        user = authenticate(
            request, username= request.POST["username"], 
            password = request.POST["password"] 
            )
        if user is not None:
            #login user
            login(request, user)
            return redirect("url_main:home")
        else:
            loggin_msg = "Please Use correct Credentials"
    return render(request, "accounts/login.html", {"msg" : loggin_msg})


def logout_user(request : HttpRequest):

    logout(request)

    return redirect("url_main:home")


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
#     return render(request, "accounts/add_info.html" )


def update_user_info(request : HttpRequest , user_id): 
    
    if not request.user.id == int(user_id):
        return render(request, "main/no_permission.html")
    user_info = Profile.objects.get(user = user_id)
    if request.method == "POST":
        _user_age = int(request.POST["age"])
        user_info.age = _user_age
        user_info.headline = request.POST["headline"]
        user_info.phone = request.POST["phone"]
        user_info.email = request.POST["email"]
        user_info.website = request.POST["website"]
        user_info.bio = request.POST["bio"]
        user_info.github = request.POST["github"]
        user_info.twitter = request.POST["twitter"]
        user_info.image = request.FILES["image"]
        user_info.save() 
        
        
        return redirect("url_main:home")
    return render(request, "accounts/update_info.html" , {"user_info" : user_info} )


def user_profile(request : HttpRequest , user_id):
    if not request.user.id == int(user_id):
        return render(request, "main/no_permission.html")
    
    users_profile = Profile.objects.get(user = user_id)
    
    context = {
        "users_profile" : users_profile
    }
    
    
    return render(request, "accounts/profiles.html" , context)


def user_info(request : HttpRequest , user_id):
    
    users_info = Profile.objects.get(user = user_id)
    context = {
        "user_info" : users_info
    }
    
    return render(request, "accounts/user_info.html" , context)