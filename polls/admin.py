from django.contrib import admin
from polls.models import Choice, Question

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #Grupirovka
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    save_as = True
    save_on_top = True
    #exclude = ['Phone']
    #readonly_fields = ['Phone']
    #raw_id_fields= ['position']

    #list_per_page = 3
    #ordering = ['Name', 'Surname']
    #list_filter = ['votes', 'question']
    search_fields = ['choice_text']
    #list_editable = ['choice_text ']
    list_display = ('question_text', 'pub_date', 'was_published_recently')

   

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)