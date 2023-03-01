from django.urls import path
from . import views


app_name = "url_customers"


urlpatterns = [
        path("customer/order/<user_id>" , views.new_orders , name = "new_orders"),
        path("customer/new_public_orders/<order_id>" , views.new_public_orders , name = "new_public_orders"),
        path("list/orders/<user_id>" , views.order_list , name = "order_list"),
        path("customer/order/update/<order_id>" , views.update_order , name = "update_order"),
        path("customer/order/delete/<order_id>" , views.delete_order , name = "delete_order"),
        path("customer/orders/list/" , views.orders_public , name = "orders_public"),
        path("customer/public/details/<order_id>" , views.order_public_details , name = "order_public_details"),
        path("customer/Comment/<order_id>" , views.add_public_comments , name = "add_public_comments"),
        path("comment/delete/<comment_id>/<order_id>" , views.delete_order_comment , name = "delete_order_comment"),
]