from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView

import mainapp
from mainapp.models import News


class MainPageView(TemplateView):
    template_name = 'index.html'


class ContactsPageView(TemplateView):
    template_name = 'contacts.html'


class CoursesPageView(TemplateView):
    template_name = 'courses_list.html'

    def get_context_data(self, **kwargs):
        context = super(CoursesPageView, self).get_context_data(**kwargs)
        context['objects'] = mainapp.models.Courses.objects.all() [:7]
        return context


class CoursesDetPageView(TemplateView):
    template_name = 'courses_detail.html'

    def get_context_data(self, pk=None, **kwargs):
        context = super(CoursesDetPageView, self).get_context_data(**kwargs)
        context['course_object'] = get_object_or_404(mainapp.models.Courses, pk=pk)
        context['lessons'] = mainapp.models.Lesson.objects.filter(course=context['course_object'])
        context['teachers'] = mainapp.models.CourseTeachers.objects.filter(course=context['course_object'])
        return context


class DocSitePageView(TemplateView):
    template_name = 'doc_site.html'


class NewsPageView(TemplateView):
    template_name = 'news.html'
    paginated_by = 3

    def get_context_data(self, **kwargs):
        page_number = self.request.GET.get(
            'page',
            1
        )
        paginator = Paginator(News.objects.all(), self.paginated_by)
        page = paginator.get_page(page_number)

        context = super().get_context_data(**kwargs)

        context['page'] = page

        return context


class NewsDetPageView(TemplateView):
    template_name = 'news_detail.html'

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(pk=pk, **kwargs)
        context['news_obj'] = get_object_or_404(mainapp.models.News, pk=pk)

        return context






