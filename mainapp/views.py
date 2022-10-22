from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import CourseFeedbackForm
import mainapp
from .models import CourseFeedback


class MainPageView(TemplateView):
    template_name = 'index.html'


class ContactsPageView(TemplateView):
    template_name = 'contacts.html'


class CoursesListView(TemplateView):
    template_name = "courses_list.html"

    def get_context_data(self, **kwargs):
        context = super(CoursesListView, self).get_context_data(**kwargs)
        context["objects"] = mainapp.models.Courses.objects.all()[:7]
        return context


class CoursesDetailView(TemplateView):
    template_name = "courses_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super(CoursesDetailView, self).get_context_data(**kwargs)
        context["course_object"] = get_object_or_404(
            mainapp.models.Courses, pk=pk
        )
        context["lessons"] = mainapp.models.Lesson.objects.filter(
            course=context["course_object"]
        )
        context["teachers"] = mainapp.models.CourseTeachers.objects.filter(
            course=context["course_object"]
        )
        if not self.request.user.is_anonymous:
            if not mainapp.models.CourseFeedback.objects.filter(
                    course=context["course_object"], user=self.request.user
            ).count():
                context["feedback_form"] = mainapp.forms.CourseFeedbackForm(
                    course=context["course_object"], user=self.request.user
                )
        context["feedback_list"] = mainapp.models.CourseFeedback.objects.filter(
            course=context["course_object"]
        ).order_by("-created", "-rating")[:5]
        return context


class CourseFeedbackFormProcessView(LoginRequiredMixin, CreateView):
    model = CourseFeedback
    form_class = CourseFeedbackForm

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object = None

    def form_valid(self, form):
        self.object = form.save()
        rendered_card = render_to_string(
            "mainapp/includes/feedback_card.html", context={"item": self.object}
        )
        return JsonResponse({"card": rendered_card})


class DocSitePageView(TemplateView):
    template_name = 'doc_site.html'


class NewsListView(ListView):
    model = mainapp.models.News
    paginate_by = 3

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class NewsCreateView(PermissionRequiredMixin, CreateView):
    model = mainapp.models.News
    fields = "__all__"
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.add_news",)


class NewsDetailView(DetailView):
    model = mainapp.models.News


class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    model = mainapp.models.News
    fields = "__all__"
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.change_news",)


class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    model = mainapp.models.News
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.delete_news",)







