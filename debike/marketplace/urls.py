from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="marketplace"),
    path("chat/<int:chat_id>/", views.chat, name="chat"),
    path("remover/<int:bike_id>", views.remover, name="remover"),
    path("anunciar/<int:bike_id>", views.anunciar, name="anunciar"),
    path("editar/<str:anuncio_codigo>", views.editar, name="editar"),
    path("comprar/<str:anuncio_codigo>", views.comprar, name="comprar"),
    path("detalhes/<str:anuncio_codigo>", views.detalhes, name="detalhes"),
]