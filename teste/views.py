from django.shortcuts import redirect, render
from django.http import HttpResponse
from teste.forms import AlunoForm, CursoForm

from teste.models import Aluno, Curso


# Create your views here.
def index(request):
    return render(request, 'inicio.html')

def novo(request):
    return HttpResponse("Essa é uma requisição")


def listarAlunos(request):
    alunos = Aluno.objects.all().order_by('nome')
    return render(request, "listar_aluno.html", {"alunos": alunos})


def listarCursos(request):
    cursos = Curso.objects.all()
    return render(request, "listar_curso.html", {"cursos": cursos})


def incluirAluno(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_alunos")
    else:
        form = AlunoForm()
    return render(request, "incluir_aluno.html", {"form": form})


def editarAluno(request, id):
    aluno = Aluno.objects.get(id=id)
    form = AlunoForm(instance=aluno)

    if request.method == "POST":
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect("listar_alunos")

    return render(request, "incluir_aluno.html", {"form": form})


def incluirCurso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_cursos")
    else:
        form = CursoForm()
    return render(request, "incluir_curso.html", {"form": form})


def editarCurso(request, id):
    curso = Curso.objects.get(id=id)
    form = CursoForm(instance=curso)

    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect("listar_cursos")

    return render(request, "incluir_curso.html", {"form": form})

def excluirAluno(request, id):
    aluno = Aluno.objects.get(id=id)
    aluno.delete()
    return redirect('listar_alunos')

def excluirCurso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect('listar_cursos')

