from django.contrib import admin
from main.models import *

# Register your models here.
class SneakersCartAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price']
class CustomerAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'last_name', 'number', 'address', 'message', 'sent_at')
# admin.site.register(SneakersCart, SneakersCartAdmin)
admin.site.register(Order)
admin.site.register(Customer, CustomerAdmin)