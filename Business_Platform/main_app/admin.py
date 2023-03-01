from django.contrib import admin
from .models import Projects ,Section,Comments , Backlog
from accounts.models import Profile , Provider , Customers 
from customers.models import Orders , CommentsOrder

admin.site.register(Projects)
admin.site.register(Comments)
admin.site.register(Section)
admin.site.register(Profile)
admin.site.register(Orders)
admin.site.register(Provider)
admin.site.register(Customers)
admin.site.register(Backlog)
admin.site.register(CommentsOrder)