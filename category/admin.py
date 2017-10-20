from django.contrib import admin

# Register your models here.

from .models import EduCategory, Tag, PostCategory


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent')  # list
    list_editable = ('name', )


class EduCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )  # list
    list_editable = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # list
    list_editable = ('name',)


admin.site.register(EduCategory, EduCategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
