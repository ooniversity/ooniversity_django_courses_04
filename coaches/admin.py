from django.contrib import admin
from django.contrib.admin import BooleanFieldListFilter

# Register your models here.
from coaches.models import Coach

class CoachAdmin(admin.ModelAdmin):
	list_display=['gender', 'skype', 'description']
	list_filter = (('is_staff', BooleanFieldListFilter),)

admin.site.register(Coach)