from django.contrib import admin
from .models import Projects ,Section,Comments
from accounts.models import Profile


admin.site.register(Projects)
admin.site.register(Comments)
admin.site.register(Section)
admin.site.register(Profile)