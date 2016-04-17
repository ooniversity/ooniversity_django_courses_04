from django.contrib import admin

# Register your models here.
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
	list_display=['name','email', 'skype']
	search_fields=['surname', 'email']
	list_filter=['courses']

admin.site.register(Student, StudentAdmin)

