from django.urls import re_path
from . import views


urlpatterns = [
    re_path('^$',  views.index, name='index'),
    re_path('relevance',  views.relevance, name='relevance'),
    re_path('geo',  views.geo, name='geo'),
    re_path('skills',  views.skills, name='skills'),
    re_path('last_vacancies',  views.last_vacancies, name='vacancies'),
]
