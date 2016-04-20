#coding:utf-8
from django.contrib import admin
from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):
    model=Coach

    def fname(request,obj):
        return obj.user.first_name
    fname.short_description = 'Name'

    def l_name(request,obj):
        return obj.user.last_name
    l_name.short_description = 'Surname'

    def _staff(request,obj):
        return obj.user.is_staff

    list_filter = ('user__is_staff',)
    list_display = ['fname', 'l_name', 'gender', 'skype', 'description']


admin.site.register(Coach, CoachAdmin)
