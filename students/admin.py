from django.contrib import admin
from students.models import Student

#class ArticleAdmin(admin.ModelAdmin):
   # prepoluted_fields = {'fullname': ('name' , 'surname')}

class StudentAdmin(admin.ModelAdmin):
    search_fields=['surname', 'email']    
    list_display = ['name' , 'surname', 'email', 'skype']
    list_filter = ['courses']
    fieldsets = [('Personal info', {'fields': ['name','surname', 'date_of_birth']}),('Contact info', {'fields': ['email','phone', 'address', 'skype', 'courses' ]})] 


    
admin.site.register(Student, StudentAdmin)
