from django.contrib import admin
from app1.models import Movies

# Register your models here.

class MoviesAdmin(admin.ModelAdmin):
    list_display = ['id','name','release_date','actor','actress','language','rating']

admin.site.register(Movies,MoviesAdmin)

