from django.contrib import admin
from .models import User,Client,Lawyer

# Register your models here.
admin.site.register(Lawyer)
admin.site.register(Client)

