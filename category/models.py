from django.db import models

# Create your models here.


class EduCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PostCategory(models.Model):
    name = models.CharField(max_length=100)
    parent = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
