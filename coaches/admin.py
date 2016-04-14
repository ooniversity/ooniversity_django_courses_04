#coding:utf-8
from django.contrib import admin
from coaches.models import Coach

class CoachAdmin(admin.ModelAdmin):
    #fullname.short_description = 'Full name'
    model=Coach
    def fname(request,obj):
        return obj.user.first_name
    fname.short_description = 'Name'
    def l_name(request,obj):
        return obj.user.last_name
    l_name.short_description = 'Surname'
    def _staff(request,obj):
        return obj.user.is_staff

    #f_name=model.user.first_name
    list_filter = ('user__is_staff',)
    list_display=['fname','l_name','gender','skype','description']
    #filter_horizontal=['courses']
    #search_fields=['surname','email']

#- list_display (выводить в admin listview следующие поля: имя, фамилия, пол, скайп, описание)

admin.site.register(Coach, CoachAdmin)
# Register your models here.
