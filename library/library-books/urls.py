from django.urls import path
from library-books.views import index, cadastro, deletarCadastro,editarCadastro

urlpatterns = [
    path('',index, name='index'),
    path('cadastro', cadastro, name='cadastro' ),
    path('deletar/<int:id>/', deletarCadastro, name='deletarCadastro'),
    path('editarCadastro/<int:id>/', editarCadastro, name='editarCadastro'),
]