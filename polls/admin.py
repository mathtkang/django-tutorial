from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {
            'fields': ['pub_date'], 
            'classes': ['collapse']
        }),
    ]
    inlines = [ChoiceInline]  
    # Choice objects are edited on the Question admin page. 
    # By default, provide enough fields for 3 choices.

# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)