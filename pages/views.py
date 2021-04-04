from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView


class JustStaticPage(TemplateView):
    # В переменной template_name обязательно указывается имя шаблона,
    # на основе которого будет создана возвращаемая страница
    template_name = 'just_page.html'
