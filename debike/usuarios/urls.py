from django.urls import path
from . import views

urlpatterns = [
    path("cadastro/", views.cadastro, name="cadastro"),
    path("cadastro_completo/", views.cadastro_completo, name="cadastro_completo"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]
