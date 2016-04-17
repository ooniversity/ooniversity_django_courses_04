from django.contrib import admin
from coaches.models import Coach

class CoachAdmin(admin.ModelAdmin):
    list_display = ['username', 'last_name', 'gender', 'skype', 'description']
    list_filter = (
        ('user__is_staff', admin.BooleanFieldListFilter),
    )

    def username(self, obj):
        return obj.user.username
    username.short_description = 'Name'

    def last_name(self, obj):
        return obj.user.last_name
    last_name.short_description = 'Last Name'

    def is_staff(self, obj):
        return obj.user.is_staff
    is_staff.short_description = 'Staff'


admin.site.register(Coach, CoachAdmin)
