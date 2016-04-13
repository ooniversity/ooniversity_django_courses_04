from courses.models import Course
from courses.models import Lesson
from django.contrib import admin

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 0

class CourseAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'short_description')
    inlines = [LessonInline]

class LessonAdmin(admin.ModelAdmin):
    list_display = ('subject', 'course')

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
