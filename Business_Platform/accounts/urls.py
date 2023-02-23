from django.urls import path
from . import views

app_name = "url_accounts"

urlpatterns = [
    path("register/", views.register_user, name="register_user"),
    path("login/", views.login_user, name="login_user"),
    path("logout/", views.logout_user, name="logout_user"),
    path("profiles/user/", views.profile_user, name="profile_user"),
]