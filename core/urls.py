from django.urls import path
from .views import inicio, Galeria, colaborador_crear,colaborador_modi,colaborador_eli


urlpatterns =[

    path ('', inicio, name="inicio"),
    path ('Galeria', Galeria, name="Galeria"),
    path ('colaborador_crear', colaborador_crear, name="colaborador_crear"),
    path ('colaborador_modi/<id>', colaborador_modi, name="colaborador_modi"),
    path ('colaborador_eli/<id>', colaborador_eli, name="colaborador_eli"),
]
