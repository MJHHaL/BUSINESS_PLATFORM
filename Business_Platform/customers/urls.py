from django.urls import path
from . import views


app_name = "url_customers"


urlpatterns = [
        path("customer/order/" , views.new_orders , name = "new_orders"),
]