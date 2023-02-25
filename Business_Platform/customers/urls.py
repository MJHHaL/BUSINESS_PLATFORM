from django.urls import path
from . import views


app_name = "url_customers"


urlpatterns = [
        path("customer/order/<user_id>" , views.new_orders , name = "new_orders"),
        path("customer/new_public_orders/<order_id>" , views.new_public_orders , name = "new_public_orders"),
        path("list/orders/<user_id>" , views.order_list , name = "order_list"),
        path("customer/order/update/<order_id>" , views.update_order , name = "update_order"),
        path("customer/order/delete/<order_id>" , views.delete_order , name = "delete_order"),
]