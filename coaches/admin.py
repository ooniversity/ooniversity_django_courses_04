from django.contrib import admin
from courses.models import Coach

class CoachAdmin(admin.ModelAdmin):
	list_display = ['first_name_field', 'last_name_field',
'gender', 'skype', 'description']
	list_fillter = ['user__is_staff']

admin.site.register(Coach, CoachAdmin)




