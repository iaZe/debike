from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre', views.sobre, name='sobre'),
    path('inicio', views.inicio, name='inicio'),
    path('restricoes', views.restricoes, name='restricoes'),
]