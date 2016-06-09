from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    search_fields = ['surname', 'email']
    list_display = ['full_name', 'email', 'skype']
    list_filter = ['courses']
    fieldsets = [
        ('Personal info', {'fields': ['name', 'surname', 'date_of_birth']}),
        ('Contact info', {'fields': ['email', 'phone', 'address', 'skype']}),
        ('', {'fields': ['courses']})]
    filter_horizontal = ['courses']

    def full_name(self, obj):
        return ('%s %s' % (obj.name, obj.surname))
    full_name.short_description = 'full name'

admin.site.register(Student, StudentAdmin)
