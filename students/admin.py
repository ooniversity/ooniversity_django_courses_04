from django.contrib import admin
from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    #ListView:
    list_display = ['full_name', 'email', 'skype']
    search_fields = ['surname', 'email']
    list_filter = ['courses']

    #ItemView:
    fieldsets = [
            ('Personal info', {'fields': ['name', 'surname', 'date_of_birth']}),
            ('Contact info', {'fields': ['email', 'phone', 'address', 'skype']}),
            (None, {'fields': ['courses']}),
        ]
    filter_horizontal = ['courses']


    def full_name(self, Student):
        return ("%s %s" % (Student.name, Student.surname))


admin.site.register(Student, StudentAdmin)