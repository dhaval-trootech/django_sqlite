from django.contrib import admin
from .models import Student


# Decorator Method...
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['stud_id', 'stud_role', 'stud_name', 'stud_address']
