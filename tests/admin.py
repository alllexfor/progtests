from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level', 'get_photo')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    readonly_fields = ('get_photo',)

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" widht="75" height="75"') 
        else:
            return 'No photo'

class WrongAnswersAdmin(admin.ModelAdmin):
    list_display = ('id', 'wrong_answer')
    list_display_links = ('id', 'wrong_answer')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'right_answer', 'language')
    list_display_links = ('id', 'question')

class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','right_answers', 'duration', 'data')
    list_display_links = ('id', 'user')



admin.site.register(Language, LanguageAdmin)
admin.site.register(WrongAnswers, WrongAnswersAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Result, ResultAdmin)
