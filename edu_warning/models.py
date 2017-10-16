from django.db import models

# Create your models here.


class HistoryWarning(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    content = models.TextField(null=True, blank=True)
    attachment = models.CharField(max_length=200, null=True, blank=True)

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


class Questionnaire(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    creator = models.ForeignKey('auth.User')
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=200)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Option(models.Model):
    title = models.CharField(max_length=50)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=20,
        choices=(
            ('single', '单选'),
        ),
        default='single',
    )
    value = models.FloatField(null=True, blank=True)
    num = models.IntegerField(default=0)
