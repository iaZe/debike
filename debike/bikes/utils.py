from django.contrib import messages

from usuarios.models import CustomUser
from .models import Bike, Venda, Historico


def bikes(user):
    return Bike.objects.filter(dono=user)


def consultar_restricao(request, codigo):
    bike = Bike.objects.filter(codigo=codigo).first()
    if not bike:
        return messages.error(request, "Bike não cadastrada")
    if bike.restricao:
        return messages.warning(request, "Bike com restrição de roubo/furto")
    else:
        return messages.success(request, "Bike sem restrições")


def realizar_venda(request, bike, form):
    cpf = form.cleaned_data["cpf"]
    valor = form.cleaned_data["valor"]

    if len(cpf) == 11:
        cpf = cpf[:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:]

    comprador = CustomUser.objects.filter(cpf=cpf).first()
    if comprador is not None:
        venda = Venda(bike=bike, comprador=comprador, valor=valor)
        venda.save()
    else:
        return messages.error(request, "Comprador não cadastrado")

    historico = Historico.objects.filter(bike=bike).first()
    if not historico:
        historico = Historico(bike=bike)
        historico.save()
    historico.adicionar_dono(bike.dono)
    historico.adicionar_venda(venda.ID)

    bike.dono = comprador
    bike.save()
    return messages.success(request, "Venda realizada com sucesso")
