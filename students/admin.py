from django.contrib import admin
from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    search_fields = ['surname', 'email']
    list_display = ('full_name', 'email', 'skype')
    list_filter = ['courses']
    fieldsets = [
        ('Personal info', {'fields': ['name', 'surname', 'date_of_birth']}),
        ('Contact info', {'fields': ['email','phone','address','skype']}),
        (None, {'fields': ['courses']}),
    ]
    filter_horizontal = ('courses',)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "courses":
            qs = kwargs.get('queryset', db_field.rel.to.objects)
            kwargs['queryset'] = qs.select_related('content_type')
        return super(StudentAdmin, self).formfield_for_manytomany(
            db_field, request=request, **kwargs)


admin.site.register(Student, StudentAdmin)
