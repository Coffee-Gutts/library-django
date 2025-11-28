from django.urls import path
from libraryBooks.views import index, cadastro

urlpatterns = [
    path('',index, name='index'),
    path('cadastro', cadastro, name='cadastro' ),
]