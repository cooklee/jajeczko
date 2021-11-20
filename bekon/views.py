from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from bekon.temp import mnozenia, get_tabliczka


def index(request):
    return HttpResponse("Witaj w świecie Django")


def index_szablon(request):
    return render(request, 'nasza_nazwe.html', )


def numbers(request, n):
    return render(request, 'numbers.html', {'numbers': [1, 2, 3, 4, 5, 6, 7, 9, 10]})


def przywitanie(request, imie):
    return render(request, 'witaj.html', {'imie': imie})


def tabliczka(request, a):
    return HttpResponse(f"podałes jako parametr {a}")


def tabliczka2(request, a, b):
    return HttpResponse(mnozenia(a, b))


def tablicza3(request, a=10, b=10):
    tab = []
    for i in range(1, a + 1):
        help = []
        for j in range(1, b + 1):
            help.append(i * j)
        tab.append(help)
    return render(request, 'tabliczka.html', {'tablica':tab})
