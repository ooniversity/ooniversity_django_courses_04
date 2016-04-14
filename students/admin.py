from django.contrib import admin
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'surname']
    list_filter = ['courses']
    list_display = ['full_name', 'email', 'skype']
    list_filter=['courses']
    filter_horizontal=['courses']
    fieldsets = [
        ("Contact info", {'fields': ['name', 'surname', 'date_of_birth']}),
        ("Personal info", {'fields': ['email', 'phone', 'address', 'skype']}),
        (None, {'fields': ['courses']})
        ]
admin.site.register(Student, StudentAdmin)
