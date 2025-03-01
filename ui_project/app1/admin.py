from django.contrib import admin
from app1.models import Student

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll_no', 'age', 'addr', 'ph_no', 'department']

admin.site.register(Student,StudentAdmin)