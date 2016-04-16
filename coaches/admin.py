from django.contrib import admin
from coaches.models import Coach
#from django.contrib.auth.models import User


class CoachAdmin(admin.ModelAdmin):    
    list_display = ['upper_case_name', 'gender', 'skype', 'description']
    def upper_case_name(self, obj):
        return ('%s %s' % (obj.user.first_name, obj.user.last_name))
    upper_case_name.short_description = "full name"
    
    list_filter = ['user__is_staff']  
admin.site.register(Coach, CoachAdmin)
