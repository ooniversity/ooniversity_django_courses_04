from django.contrib import admin
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
    search_fields=['surname', 'email']
    list_display=['fullname', 'email', 'skype']
    list_filter=['courses']
    fieldsets = (
        ('Personal info', {
            'fields': ('name', 'surname', 'date_of_birth')
        }),
        ('Contact info', {
            'fields': ('email', 'phone', 'address', 'skype','courses')
        }),    
    )
    filter_horizontal=['courses']
    def fullname(self, Student):
        return ("%s %s" % (Student.name, Student.surname))

admin.site.register(Student, StudentAdmin)
