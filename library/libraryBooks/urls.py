from django.urls import path
from libraryBooks.views import deletar, index, cadastro, editar

urlpatterns = [
    path('',index, name='index'),
    path('cadastro', cadastro, name='cadastro' ),
    path('editar/<int:id>', editar, name='editar' ),
    path('deletar/<int:id>', deletar, name='deletar'),
]