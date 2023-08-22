from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.urls import reverse

from .forms import CustomUserCompleteForm
from .models import CustomUser
from .utils import save_user


# Create your views here.
def cadastro(request):
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")

        user_exists = CustomUser.objects.filter(email=email).exists()
        if user_exists:
            messages.error(request, "Usuário já cadastrado")
            return redirect(reverse("cadastro"))

        if senha != confirmar_senha:
            messages.error(request, "Senhas não conferem")
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

        if form.is_valid():
            save_user(form)
            messages.success(request, "Cadastro completo")
            return redirect(reverse("inicio"))
        else:
            messages.error(request, "Erro ao completar cadastro")
            return redirect(reverse("cadastro_completo"))
    else:
        form = CustomUserCompleteForm(instance=user)
        return render(request, "cadastro_completo.html", {"form": form})


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username=username, password=password)
        if not user:
            messages.error(request, "Usuário ou senha inválidos")
            return redirect(reverse("login"))

        auth.login(request, user)
        if user.first_login:
            messages.error(request, "Complete seu cadastro")
            return redirect(reverse("cadastro_completo"))
        return redirect(reverse("inicio"))
    else:
        return render(request, "login.html")


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado")
    return redirect(reverse("login"))
