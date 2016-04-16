from django.contrib import admin
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
	list_display = ('Full_name','email', 'skype')
	search_fields = ['surname', 'email']
admin.site.register(Student, StudentAdmin)
