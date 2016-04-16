from django.contrib import admin
from students.models import Student


def get_fullname(student):
    return "%s %s" % (student.name, student.surname)


class StudentAdmin(admin.ModelAdmin):
    search_fields = ['surname', 'email']
    list_filter = ['courses']
    list_display = [get_fullname, 'email', 'skype']
    filter_horizontal = ('courses',)
    fieldsets = [
       ('Personal info', {'fields': ('name', 'surname', 'date_of_birth',)}),
       ('Contact info', {'fields': ('email', 'phone', 'address', 'skype',)}),
       (None, {'fields': ('courses',)})
    ]


admin.site.register(Student, StudentAdmin)
