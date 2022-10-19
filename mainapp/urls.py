from django.urls import path
from .views import *

from mainapp.apps import MainappConfig

app_name = MainappConfig.name


urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('courses_list/', CoursesPageView.as_view(), name='courses_list'),
    path('courses/<int:pk>', CoursesDetPageView.as_view(), name='courses_detail'),
    path('doc_site/', DocSitePageView.as_view(), name='doc_site'),
    path('news/', NewsPageView.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetPageView.as_view(), name='news_detail'),
]