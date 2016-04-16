from django.contrib import admin
from students.models import Student



class StudentAdmin(admin.ModelAdmin):
    search_fields=['surname', 'email']    
    list_display = ['name' , 'surname', 'email', 'skype']



admin.site.register(Student, StudentAdmin)

