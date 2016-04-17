from django.contrib import admin
from coaches.models import Coach
#from django.contrib.admin import BooleanFieldListFilter

class CoachAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'skype', 'description']
    list_filter = [['user__is_staff', admin.BooleanFieldListFilter]]


admin.site.register(Coach, CoachAdmin)
