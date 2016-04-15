from django.contrib import admin
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
	def fullname(self, obj):
		return " ".join((obj.name, obj.surname))
	fullname.short_description = 'Full name'

	list_display = ['fullname', 'email', 'skype']
	search_fields = ['surname', 'email']
	list_filter = ('courses',)
	filter_horizontal = ['courses']
	fieldsets = (('Personal info', {'fields':('name', 'surname', 'date_of_birth',)}),
				('Contact info', {'fields':('email', 'phone', 'address', 'skype',)}),
				(None, {'fields':('courses',)}),
				)

admin.site.register(Student, StudentAdmin)

