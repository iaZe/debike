from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from bikes.utils import bikes
from marketplace.utils import anunciadas

# Create your views here.
def index(request):
    return render(request, "index.html")

def restricoes(request):
    return render(request, "restricoes.html")

def sobre(request):
    return render(request, "sobre.html")

@login_required
def inicio(request):
    return render(request, "inicio.html", {"bikes": bikes(request.user)})
