from django.views.generic import TemplateView
from datetime import datetime


class MainPageView(TemplateView):
    template_name = 'index.html'


class ContactsPageView(TemplateView):
    template_name = 'contacts.html'


class CoursesPageView(TemplateView):
    template_name = 'courses_list.html'


class DocSitePageView(TemplateView):
    template_name = 'doc_site.html'


class LoginPageView(TemplateView):
    template_name = 'login.html'


class NewsPageView(TemplateView):
    template_name = 'news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['news_title'] = 'Новость'
        context['news_text'] = 'Предварительное описание новости'
        context['news_date'] = datetime.now()
        context['range'] = range(5)

        return context


class NewsWithPaginatorView(NewsPageView):
    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context['page_num'] = page
        return context


