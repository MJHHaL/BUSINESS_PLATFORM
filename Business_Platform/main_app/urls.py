from django.urls import path
from . import views


app_name = "url_main"


urlpatterns = [
    
    path("" , views.index , name = "home"),
    path("control_panel/<user_id>" , views.provider_panel , name = "provider_panel"),
    path("project/add/" , views.add_projects , name = "add_projects"),
    path("project/update/<project_id>" , views.update_project , name = "update_project"),
    path("project/details/<project_id>" , views.project_details , name = "project_details"),
    path("project/delete/<project_id>" , views.delete_project , name = "delete_project"),
    path("comment/delete/<comment_id>" , views.delete_comment , name = "delete_comment"),
    path("project/Comment/<project_id>" , views.add_Comments , name = "add_comments"),
    # path("project/profile/add/info" , views.user_info , name = "user_info"),
    path("profiles/user/", views.profile_user, name="profile_user"),
    path("project/orders/<user_id>", views.orders_received, name="orders_received"),
    path("project/most/", views.most_comment, name="most_comment"),
    path("project/section/<section_num>", views.order_by_section, name="order_by_section"),
]