from django.contrib import admin
from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    search_fields = ['surname', 'email']
    list_filter = ['courses']
    list_display = ['full_name', 'email', 'skype']
    filter_horizontal = ('courses',)
    fieldsets = [
       ('Personal info', {'fields': ('name', 'surname', 'date_of_birth',)}),
       ('Contact info', {'fields': ('email', 'phone', 'address', 'skype',)}),
       (None, {'fields': ('courses',)})
    ]

    @staticmethod
    def full_name(student):
        return "%s %s" % (student.name, student.surname)

admin.site.register(Student, StudentAdmin)
