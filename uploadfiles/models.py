from django.db import models
from edu_warning.models import HistoryWarning

# Create your models here.


class UploadFile(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    file = models.FileField(upload_to="uploads/%Y/%m")
    date = models.DateField(auto_now_add=True)
    festival = models.ForeignKey(HistoryWarning, on_delete=models.CASCADE, null=True)
