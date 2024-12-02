from django.contrib import admin
from .models import Question, Choice
from django.utils import timezone
import datetime
# Register your models here.

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionModelAdmin(admin.ModelAdmin):
    '''Admin View for QuestionModel'''

    list_display = ('question_text','published_at','was_published_recently')
    list_filter = ('published_at',)
    search_fields = ('quesiton_text',)
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['published_at'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]
    
    
from django.contrib import admin


admin.site.register(Question, QuestionModelAdmin)
admin.site.register(Choice)