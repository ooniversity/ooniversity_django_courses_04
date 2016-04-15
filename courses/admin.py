# encoding: utf-8
from django.contrib import admin
from courses.models import Course, Lesson

class LessonInline(admin.TabularInline):
    model = Lesson

class CourseAdmin(admin.ModelAdmin):

    """custom view for course_admin"""

    list_display = ('name', 'short_description')
    search_fields =('name',)
    inlines = [LessonInline]

admin.site.register(Course,  CourseAdmin)
admin.site.register(Lesson)
