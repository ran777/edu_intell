from django.contrib import admin

# Register your models here.

from .models import HistoryWarning


class HistoryWarningAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'str_edu_category', 'str_tags', 'post_category')


admin.site.register(HistoryWarning, HistoryWarningAdmin)
