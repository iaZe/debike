from django.db import models
from usuarios.models import CustomUser

import json

# Create your models here.
class Bike(models.Model):
    ID = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=30, unique=True)
    modelo = models.CharField(max_length=50)
    cor = models.CharField(max_length=20)
    dono = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    foto = models.FileField(upload_to="fotos", blank=True)
    restricao = models.BooleanField(default=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.modelo

class Venda(models.Model):
    ID = models.AutoField(primary_key=True)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    comprador = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_venda = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bike.modelo + " - " + self.comprador.username
    
class Historico(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    donos = models.TextField(default="[]")
    vendas = models.TextField(default="[]")
    data_atualizacao = models.DateTimeField(auto_now=True)

    def adicionar_dono(self, dono):
        historico_donos = json.loads(self.donos)
        historico_donos.append(dono.username)
        self.donos = json.dumps(historico_donos)
        self.save()

    def adicionar_venda(self, venda):
        historico_vendas = json.loads(self.vendas)
        historico_vendas.append(venda)
        self.vendas = json.dumps(historico_vendas)
        self.save()
    
    def __str__(self):
        return self.bike.modelo + " - " + self.bike.dono.username
