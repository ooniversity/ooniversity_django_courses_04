from django.contrib import admin
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'skype')
admin.site.register(Student)
