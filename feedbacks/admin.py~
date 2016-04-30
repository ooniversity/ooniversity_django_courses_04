from django.contrib import admin
from feedbacks.models import Feedback



class FeedbackAdmin(admin.ModelAdmin):
           
    list_display = ['from_email', 'create_date']
    #def case_name(self, obj):
    #    return ('%s %s' % (obj.name, obj.surname))
    #case_name.short_description = "full name"

    
admin.site.register(Feedback, FeedbackAdmin)
