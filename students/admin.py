from django.contrib import admin

from students.models import Student


class StudentsAdmin(admin.ModelAdmin):
    def fullname(self,obj):
        return "%s %s" % (obj.name, obj.surname)

    search_fields = ['surname', 'email']
    list_filter = ['courses']
    list_display = ['fullname', 'email', 'skype']
    filter_horizontal = ['courses']
    fieldsets = [
       ('Personal info', {'fields': ('name','surname','date_of_birth',)}),
       ('Contact info', {'fields': ('email','phone','address','skype',)}),
       (None, {'fields': ('courses',)})
    ]

admin.site.register(Student, StudentsAdmin)
