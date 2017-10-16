from django.contrib import admin

# Register your models here.

from .models import HistoryWarning, Questionnaire, Question, Option


class HistoryWarningAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'str_edu_category', 'str_tags', 'post_category')


class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'creator', 'start_date', 'end_date',)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'questionnaire',)


class OptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'title', 'type', 'value')


admin.site.register(HistoryWarning, HistoryWarningAdmin)
admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Option, OptionAdmin)
