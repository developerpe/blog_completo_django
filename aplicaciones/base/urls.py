from django.urls import path
from .views import Inicio,Listado,FormularioContacto,DetallePost,Suscribir

urlpatterns = [
    path('',Inicio.as_view(), name = 'index'),
    path('videojuegos/',Listado.as_view(),{'nombre_categoria':'Videojuegos'}, name = 'videojuegos'),
    path('generales/',Listado.as_view(),{'nombre_categoria':'General'}, name = 'generales'),
    path('formulario_contacto/', FormularioContacto.as_view(), name = 'formulario_contacto'),
    path('suscribirse/',Suscribir.as_view(), name = 'suscribirse'),
    path('<slug:slug>/',DetallePost.as_view(), name = 'detalle_post'),
]
