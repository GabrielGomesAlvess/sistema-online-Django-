from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Ola, mundo! Agora é na web.")


def novo(request):
    return HttpResponse("Essa é uma requisição")
