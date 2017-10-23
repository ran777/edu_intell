from django.contrib import admin
from .models import UploadFile
# Register your models here.


class UploadFileInline(admin.TabularInline):
    model = UploadFile
