from django.contrib import admin
from students.models import Student
from django.db import models
from django.contrib.admin.widgets import FilteredSelectMultiple

class StudentAdmin(admin.ModelAdmin):
    search_fields = ['surname', 'email']
    list_display = ('full_name','email', 'skype',)
    list_filter = ['courses']

    def full_name(self, Student):
        return ("%s %s" % (Student.name, Student.surname)).upper()
    full_name.short_description = 'Full name'
    fieldsets = [('Personal info', {'fields':['name', 'surname', 'date_of_birth']}),
                 ('Contact info', {'fields':['email', 'phone', 'address', 'skype']}),
                 (None, {'fields':['courses']}),]
    item_filter = ['courses']
    formfield_overrides = {models.ManyToManyField:{'widget':FilteredSelectMultiple("verbose name", is_stacked=False)}}


admin.site.register(Student, StudentAdmin)