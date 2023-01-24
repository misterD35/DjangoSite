from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['ВИДЫ', 'Количество', '123'],
        'obj': {
            'tree': 'Ель',
            'class': 'Хвойные',
            'life': 250
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def catalog(request):
    return HttpResponse("<h4>Каталог товаров</h4")


def services(request):
    return HttpResponse("<h4>Наши услуги</h4")