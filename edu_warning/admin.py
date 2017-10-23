from django.contrib import admin
import nested_admin
# Register your models here.

from .models import HistoryWarning, Questionnaire, Question, Option
from uploadfiles.admin import UploadFileInline


@admin.register(HistoryWarning)
class HistoryWarningAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'str_edu_category', 'str_tags', 'post_category')
    inlines = [UploadFileInline]


class OptionInline(nested_admin.NestedTabularInline):
    fields = ('title', 'value', 'num')
    readonly_fields = ('num', )
    model = Option


class QuestionInline(nested_admin.NestedStackedInline):
    inlines = [OptionInline]
    model = Question


@admin.register(Questionnaire)
class QuestionnaireAdmin(nested_admin.NestedModelAdmin):
    list_display = ('title', 'creator', 'end_date', 'population', 'status')
    list_display_links = ('title',)
    fields = ('title', 'creator', 'population', 'status', 'start_date', 'end_date', 'content',)
    readonly_fields = ('creator', 'population')
    list_filter = ('creator', 'status')
    search_fields = ('title',)
    inlines = [QuestionInline]
