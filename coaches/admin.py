from django.contrib import admin
from .models import Coach


class CoachAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'gender', 'skype', 'description']
    list_filter = ['user__is_staff']

    def full_name(self, obj):
        return ('%s %s' % (obj.user.first_name, obj.user.last_name))
    full_name.short_description = 'full name'

admin.site.register(Coach, CoachAdmin)
