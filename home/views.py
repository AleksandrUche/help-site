from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


# домашняя страница


class HomeView(TemplateView):
    template_name = 'home/home.html'
    extra_context = {'title': 'Главная страница'}


def about(request):
    return render(request, 'home/about.html', {'title': 'О сайте'})


def contact(request):
    return HttpResponse("Обратная связь")
