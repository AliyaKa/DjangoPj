from django.contrib import admin
from mainapp import models as mainapp_models
from django.utils.translation import gettext_lazy as _


@admin.register(mainapp_models.News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ["title", "preamble", "body"]


@admin.register(mainapp_models.Lesson)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["id", "num", "title", "deleted"]
    ordering = ["-course__name", "-num"]
    list_per_page = 10
    list_filter = ["course", "created", "deleted"]
    actions = ["mark_deleted"]

    def get_course_name(self, obj):
        return obj.course.name

    get_course_name.short_description = _("Courses")

    def mark_deleted(self, request, queryset):
        queryset.update(deleted=True)

    mark_deleted.short_description = _("Mark deleted")
