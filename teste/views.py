from django.shortcuts import render
from django.http import HttpResponse

from teste.models import Aluno, Curso


# Create your views here.
def index(request):
    return HttpResponse("Ola, mundo! Agora é na web.")


def novo(request):
    return HttpResponse("Essa é uma requisição")


def listarAlunos(request):
    alunos = Aluno.objects.all()
    return render(request, "listar_aluno.html", {"alunos": alunos})


def listarCursos(request):
    cursos = Curso.objects.all()
    return render(request, "listar_curso.html", {"cursos": cursos})
