from django.contrib import admin
from .models import Projects ,Section,Comments
from accounts.models import Profile , Provider
from customers.models import Orders

admin.site.register(Projects)
admin.site.register(Comments)
admin.site.register(Section)
admin.site.register(Profile)
admin.site.register(Orders)
admin.site.register(Provider)