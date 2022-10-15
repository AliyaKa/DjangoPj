from django.db import models
from mainapp.managers.news_manager import NewsManager


class News(models.Model):
    objects = NewsManager()
    title = models.CharField(max_length=256, verbose_name='title')
    preamble = models.CharField(max_length=1024, blank=True, null=True, verbose_name='Preamble')
    body = models.TextField(blank=False, null=False, verbose_name='Body')
    body_as_markdown = models.BooleanField(
        default=False,
        verbose_name='As markdown'
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date of creating',
        editable=False
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Date of editing',
        editable=False
    )
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def delete(self, *args):
        self.deleted = True
        self.save()

class Courses(models.Model):
    name = models.CharField(max_length=256, verbose_name='Name')
    description = models.TextField(blank=False, null=False, verbose_name='Description')
    description_as_markdown = models.BooleanField(
        default=False,
        verbose_name='As markdown'
    )
    cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Cost', default=0)
    cover = models.CharField(max_length=25, default="no_image.svg", verbose_name="Cover")

    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date of creating',
        editable=False
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Date of editing',
        editable=False
    )
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def delete(self, *args):
        self.deleted = True
        self.save()


class Lesson(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    num = models.PositiveIntegerField(verbose_name="Lesson number")
    title = models.CharField(max_length=256, verbose_name="Name")
    description = models.TextField(
        verbose_name="Description", blank=True, null=True
    )
    description_as_markdown = models.BooleanField(
        verbose_name="As markdown", default=False
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date of creating',
        editable=False
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Date of editing',
        editable=False
    )
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.course.name} | {self.num} | {self.title}"

    def delete(self, *args):
        self.deleted = True
        self.save()

    class Meta:
        ordering = ("course", "num")


class CourseTeachers(models.Model):
    course = models.ManyToManyField(Courses)
    name_first = models.CharField(max_length=128, verbose_name="Name")
    name_second = models.CharField(max_length=128, verbose_name="Surname")
    birthday = models.DateField(verbose_name="Birth date")
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name_second, self.name_first

    def delete(self, *args):
        self.deleted = True
        self.save()