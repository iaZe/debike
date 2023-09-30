from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse

from django.utils.safestring import mark_safe

from bikes.models import Bike
from usuarios.models import CustomUser
from .forms import AnuncioForm
from .models import Anuncio, Chat, Messages
from .utils import verificacoes


def index(request):
    if request.method == "GET":
        anuncios = Anuncio.objects.all()
        return render(request, "marketplace.html", {"anuncios": anuncios})


@login_required
def anunciar(request, bike_id):
    if request.method == "GET":
        if verificacoes(request, bike_id):
            form = AnuncioForm()
            return render(request, "anunciar.html", {"form": form})
        else:
            return redirect(reverse("inicio"))

    elif request.method == "POST":
        form = AnuncioForm(request.POST, request.FILES)
        if form.is_valid():
            anuncio = form.save(commit=False)
            anuncio.usuario = CustomUser.objects.get(id=request.user.id)
            anuncio.bike = Bike.objects.get(ID=bike_id)
            anuncio.save()
            Bike.objects.filter(ID=bike_id).update(marketplace=True)
            messages.success(request, "Anúncio criado com sucesso")
            return redirect("marketplace")
        else:
            messages.error(request, "Erro ao criar anúncio")
            return render(request, "anunciar.html", {"form": form})


def detalhes(request, anuncio_codigo):
    if request.method == "GET":
        if Anuncio.objects.filter(codigo=anuncio_codigo).exists():
            anuncio = Anuncio.objects.get(codigo=anuncio_codigo)
            return render(request, "detalhes.html", {"anuncio": anuncio})
        else:
            return redirect(reverse("inicio"))


@login_required
def editar(request, anuncio_codigo):
    if request.method == "GET":
        if Anuncio.objects.filter(ID=anuncio_codigo).exists():
            anuncio = Anuncio.objects.get(ID=anuncio_codigo)
            if anuncio.usuario == request.user:
                form = AnuncioForm(instance=anuncio)
                return render(request, "editar.html", {"form": form})
            else:
                return redirect(reverse("inicio"))
        else:
            return redirect(reverse("inicio"))

    elif request.method == "POST":
        anuncio = Anuncio.objects.get(ID=anuncio_codigo)
        form = AnuncioForm(request.POST, request.FILES, instance=anuncio)
        if form.is_valid():
            form.save()
            return redirect(
                reverse("detalhes", kwargs={"anuncio_codigo": anuncio_codigo})
            )
        else:
            messages.error(request, "Erro ao editar anúncio")
            return render(request, "editar.html", {"form": form})


@login_required
def remover(request, bike_id):
    if request.method == "GET":
        if Anuncio.objects.filter(bike=bike_id).exists():
            anuncio = Anuncio.objects.get(bike=bike_id)
            if anuncio.usuario == request.user:
                anuncio.delete()
                Bike.objects.filter(ID=bike_id).update(marketplace=False)
                return redirect(reverse("inicio"))
            else:
                return redirect(reverse("inicio"))
        else:
            return redirect(reverse("inicio"))


@login_required
def comprar(request, anuncio_codigo):
    anuncio = get_object_or_404(Anuncio, codigo=anuncio_codigo)

    if request.user == anuncio.usuario:
        messages.error(request, "Você não pode comprar seu próprio anúncio")
        return redirect(reverse("inicio"))

    chat = Chat.objects.filter(
        anuncio=anuncio, comprador=request.user, vendedor=anuncio.usuario
    )
    if not chat:
        chat = Chat.objects.create(
            anuncio=anuncio, comprador=request.user, vendedor=anuncio.usuario
        )
    else:
        chat = chat[0]
    return redirect(reverse("chat", kwargs={"chat_id": chat.id}))


@login_required
def chat(request, chat_id):
    if request.method == "GET":
        chats = Chat.objects.filter(comprador=request.user) | Chat.objects.filter(vendedor=request.user)
        if chat_id == 0:
            # redirecionar o último chat do usuário, caso ele tenha mais de um
            if chats:
                chat = chats[len(chats) - 1]
                return redirect(reverse("chat", kwargs={"chat_id": chat.id}))
            else:
                #apresenta o chat 0, caso o usuário não tenha nenhum chat
                chat = "Sistema"
                message = mark_safe(
                "Você não possui chats abertos, que tal buscar novos produtos clicando <a href='{% url 'marketplace' %}'>aqui</a>?"
                )
                messages = [{"sender": "admin", "message": message}]

                return render(
                    request,
                    "chat.html",
                    {"chat": chat, "messages": messages, "last_message": message},
                )
        else:
            chat = get_object_or_404(Chat, id=chat_id)

        if chat.vendedor != request.user and chat.comprador != request.user:
            return redirect(reverse("inicio"))
        
        message_instance, created = Messages.objects.get_or_create(chat=chat)
        messages = message_instance.get_historico()
        for message in messages:
            if message["sender"] == request.user.username:
                message["sender"] = True

        return render(
            request,
            "chat.html",
            {
                "chat": chat,
                "chats": chats,
                "messages": messages,
            },
        )
        
    if request.method == "POST":
        chat = get_object_or_404(Chat, id=chat_id)
        if request.user == chat.comprador or request.user == chat.vendedor:
            if not Messages.objects.filter(chat=chat).exists():
                Messages.objects.create(chat=chat)
            else:
                Messages.objects.get(chat=chat)
            message = Messages.objects.get(chat=chat)
            message.adicionar_mensagem(
                {
                    "sender": request.user.username,
                    "message": request.POST["message"],
                    "date": message.date.strftime("%d/%m/%Y %H:%M"),
                }
            )

            return redirect(reverse("chat", kwargs={"chat_id": chat_id}))
        else:
            messages.error(request, "Você não tem permissão para acessar este chat")
            return redirect(reverse("inicio"))
