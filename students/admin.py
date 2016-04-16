from django.contrib import admin
from students.models import Student



class StudentAdmin(admin.ModelAdmin):
    search_fields=['surname', 'email']    
    list_display = ['name' , 'surname', 'email', 'skype']
    #list_filter = ['course']
    fieldsets = [('Personal info', {'fields': ['name','surname', 'date_of_birth']}),('Contact info', {'fields': ['email','phone', 'address', 'skype', 'courses' ]})] 
    
admin.site.register(Student, StudentAdmin)
