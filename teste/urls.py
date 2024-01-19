from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("outro", views.novo, name="novo"),
    # Aluno
    path("listar_alunos", views.listarAlunos, name="listar_alunos"),
    path("incluir_aluno", views.incluirAluno, name="incluir_aluno"),
    # Curso
    path("listar_cursos", views.listarCursos, name="listar_cursos"),
    path("incluir_curso", views.incluirCurso, name="incluir_curso"),
    # Editar
    path("editar_aluno/<int:id>", views.editarAluno, name="editar_aluno"),
    path("editar_curso/<int:id>", views.editarCurso, name="editar_curso"),
    # Excluir
    path("excluir_aluno/<int:id>", views.excluirAluno, name="excluir_aluno"),
    path("excluir_curso/<int:id>", views.excluirCurso, name="excluir_curso")
]
