from django.contrib import admin
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
	search_fields = ['surname', 'email']
	list_display = ['full_name', 'email', 'skype', ]

	def full_name(request, Student):
	    return "%s %s" % (Student.name, Student.surname)	

	list_filter = ['courses']
	

admin.site.register(Student, StudentAdmin)

