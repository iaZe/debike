from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.urls import reverse
from django.http import JsonResponse

import requests

from .forms import CustomUserCompleteForm
from .models import CustomUser
from .utils import save_user, validate_email, validate_password, validate_cpf, validate_telefone


# Create your views here.
def cidades_por_estado(request, uf):
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        cidades = [cidade['nome'] for cidade in data]
        return JsonResponse({"cidades": cidades})
    else:
        return JsonResponse({'error': 'Erro ao buscar cidades'}, status=500)

def cadastro(request):
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")

        if not validate_email(request, email):
            return redirect(reverse("cadastro"))
        
        if validate_password(request, senha, confirmar_senha) != True:
            return redirect(reverse("cadastro"))

        try:
            user = CustomUser(username=email, email=email)
            user.set_password(senha)
            user.save()
            messages.success(request, "Usuário cadastrado com sucesso")
            return redirect(reverse("cadastro_completo"))
        except Exception as e:
            messages.error(request, "Erro ao cadastrar usuário")
            return redirect(reverse("cadastro"))
    else:
        return render(request, "cadastro.html")


@login_required
def cadastro_completo(request):
    user = request.user
    if request.method == "POST":
        form = CustomUserCompleteForm(request.POST, instance=user)

        if not validate_cpf(request, request.POST.get("cpf")):
            return redirect(reverse("cadastro_completo"))
        
        if not validate_telefone(request, request.POST.get("telefone")):
            return redirect(reverse("cadastro_completo"))

        if form.is_valid():
            cadastro = form.save(commit=False)
            cadastro.first_login = False
            cadastro.save()
            messages.success(request, "Cadastro completo")
            return redirect(reverse("inicio"))
        else:
            messages.error(request, "Erro ao completar cadastro")
            return redirect(reverse("cadastro_completo"))
    else:
        form = CustomUserCompleteForm(instance=user)
        return render(request, "cadastro_completo.html", {"form": form, "user": user})


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        username = username.lower()

        user = auth.authenticate(username=username, password=password)
        if not user:
            messages.error(request, "Usuário ou senha inválidos")
            return redirect(reverse("login"))

        auth.login(request, user)
        if user.first_login:
            return redirect(reverse("cadastro_completo"))
        return redirect(reverse("inicio"))
    else:
        if request.user.is_authenticated:
            return redirect(reverse("inicio"))
        return render(request, "login.html")


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado")
    return redirect(reverse("login"))
