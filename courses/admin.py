from django.contrib import admin

# Register your models here.
from courses.models import Course
from courses.models import Lesson

class LessonInline(admin.StackedInline):
	model = Lesson
	list_display=['subject', 'description', 'order']

class CourseAdmin(admin.ModelAdmin):
	list_display=['name', 'short_description']
	search_fields=['name']
	inlines=[LessonInline]



admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)


