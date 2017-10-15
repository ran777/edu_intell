from django.contrib import admin

# Register your models here.

from .models import EduCategory, Tag, PostCategory


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent')  # list


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # list


admin.site.register(EduCategory)
admin.site.register(Tag, TagAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
