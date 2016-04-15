# encoding: utf-8
from django.contrib import admin
from students.models import Student

def fullname(obj):
    return ("{} {}".format(obj.name, obj.surname))
    fullname.short_description = "full name"


class StudentAdmin(admin.ModelAdmin):
    """custom view for Student_admin"""

    list_display = (fullname, 'email', 'skype')
    list_filter = ['courses']
    search_fields = ['surname', 'email']
    filter_horizontal = ('courses',)
    fieldsets = [('Personal info', {'fields': ['name', 'surname', 'date_of_birth']}),
        ('Contact info', {'fields': ['email', 'phone', 'address', 'skype']}),
        (None, {'fields': ['courses']}),]


admin.site.register(Student, StudentAdmin)
