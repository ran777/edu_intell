from django.db import models
# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    content = models.TextField(null=True, blank=True)

    edu_category = models.ManyToManyField(
        'category.EduCategory',
        )

    tag = models.ManyToManyField(
        'category.Tag',
        blank=True,
        )

    post_category = models.ForeignKey(
        'category.PostCategory',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def list_edu_category(self):
        return [p.name for p in self.edu_category.all()]

    def list_tags(self):
        return [p.name for p in self.tag.all()]

    def str_edu_category(self):
        return "/".join(self.list_edu_category())

    def str_tags(self):
        return "/".join(self.list_tags())