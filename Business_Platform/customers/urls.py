from django.urls import path
from . import views


app_name = "url_customers"


urlpatterns = [
        path("customer/order/<user_id>" , views.new_orders , name = "new_orders"),
]