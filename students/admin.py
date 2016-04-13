from django.contrib import admin

from students.models import Student

class LessonInline(admin.TabularInline):
    #model = Lesson
    #extra=0
    pass


class StudentAdmin(admin.ModelAdmin):
    def fullname(self,obj):
        return " ".join((obj.name,obj.surname))
    fullname.short_description = 'Full name'
    list_filter = ('courses',)
    list_display=['fullname','email','skype']
    filter_horizontal=['courses']
    search_fields=['surname','email']
    fieldsets=(
       ('Personal info',{'fields':('name','surname','date_of_birth',)}),
       ('Contact info',{'fields':('email','phone','address','skype',)}),
       (None,{'fields':('courses',)}),
       )

admin.site.register(Student,StudentAdmin)

