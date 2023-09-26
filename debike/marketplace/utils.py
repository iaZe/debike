from django.shortcuts import redirect
from django.contrib import messages

from bikes.models import Bike
from .models import Anuncio

def anunciadas(request):
    anunciadas = Anuncio.objects.filter(usuario_id=request.user.id)
    return anunciadas

def verificacoes(request, bike_id):
    if not Bike.objects.filter(ID=bike_id).exists():
        return messages.error(request, "Bike não encontrada")
    elif Anuncio.objects.filter(bike=bike_id).exists():
        return messages.error(request, "Bike anunciada")
    elif not Bike.objects.filter(ID=bike_id, dono_id=request.user.id).exists():
        return messages.error(request, "Bike não pertence ao usuário")
    elif Bike.objects.filter(ID=bike_id, restricao=True).exists():
        return messages.error(request, "Bike restrita")
    else:
        return True
    