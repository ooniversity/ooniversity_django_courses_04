from django.contrib import admin
from coaches.models import Coach

class CoachAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'skype', 'description']
    list_filter = ['user__is_staff',]
    def first_name(self, Coach):
        return Coach.user.first_name
    def last_name(self, Coach):
        return Coach.user.last_name

admin.site.register(Coach, CoachAdmin)

