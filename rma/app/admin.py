from django.contrib import admin
from .models import *

class OrderAdmin(admin.ModelAdmin):
    list_display = ["code", "client_name"]

admin.site.register(Order, OrderAdmin)

# Register your models here.
