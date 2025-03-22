from django.contrib import admin
from app1.models import Product
from app1.models import User

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','category']

admin.site.register(Product, ProductAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username', 'password']

admin.site.register(User,UserAdmin)