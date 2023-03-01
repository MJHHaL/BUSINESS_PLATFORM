from django.urls import path
from . import views

app_name = "url_accounts"

urlpatterns = [
    path("register/", views.register_user, name="register_user"),
    path("login/", views.login_user, name="login_user"),
    path("logout/", views.logout_user, name="logout_user"),
    path("profiles/user/<user_id>", views.user_profile, name="user_profile"),
    # path("profile/add/info/" , views.user_info , name = "user_info"),
    path("profile/update/info/<user_id>" , views.update_user_info , name = "update_user_info"),
    path("profile/info/<user_id>" , views.user_info , name = "user_info"),
]