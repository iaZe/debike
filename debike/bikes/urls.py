from django.urls import path
from . import views

urlpatterns = [
    path("cadastrar", views.cadastrar, name="cadastrar_bike"),
    path("consultar", views.consultar, name="consultar_bike"),
    path("vender/<str:codigo>", views.vender, name="vender_bike"),
    path("restringir/<str:codigo>", views.restringir, name="restringir_bike"),
    path("excluir/<str:codigo>", views.excluir, name="excluir_bike"),
]