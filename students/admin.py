from django.contrib import admin
from students.models import Student



class StudentAdmin(admin.ModelAdmin):
    search_fields=['surname', 'email']        
    list_display = ['upper_case_name', 'email', 'skype']
    def upper_case_name(self, obj):
        return ('%s %s' % (obj.name, obj.surname))
    upper_case_name.short_description = "full name"
    list_filter = ['courses']
    fieldsets = [('Personal info', {'fields': ['name','surname', 'date_of_birth']}),('Contact info', {'fields': ['email','phone', 'address', 'skype']}), ( '',{'fields': ['courses']})]
    filter_horizontal = ['courses'] 


    
admin.site.register(Student, StudentAdmin)
