from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("outro", views.novo, name="novo"),
    # Aluno
    path("listar_alunos", views.listarAlunos, name="listar_alunos"),
    # Curso
    path("listar_cursos", views.listarCursos, name="listar_cursos"),
]
