from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from bekon.temp import mnozenia


def index(request):
    return HttpResponse("Witaj w świecie Django")


def tabliczka(request, a):
    return HttpResponse(f"podałes jako parametr {a}")

def tabliczka2(request, a, b):
    return HttpResponse(mnozenia(a, b))


