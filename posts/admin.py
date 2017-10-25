from django.contrib import admin

# Register your models here.

from .models import Posts

@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'str_edu_category', 'str_tags', 'post_category')
