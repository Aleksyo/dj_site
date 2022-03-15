from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Приложение Women")


def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Категория {catid}</h1>")


def archive(request, year):
    if int(year) > 2020:
        # raise Http404()
        return redirect('home')
    return HttpResponse(f'Архив за {year}')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h2>Страница не найдена</h2>')
