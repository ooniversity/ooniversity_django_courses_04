from django.contrib import admin
from courses.models import Course, Lesson


class Lessoninline(admin.TabularInline):
    model = Lesson
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "short_description"]
    search_fields = ["name"]
    inlines = [Lessoninline]

admin.site.register(Course, CourseAdmin)
