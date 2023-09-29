from django.db import models
from django.utils.crypto import get_random_string

import json

# Create your models here.
class Anuncio(models.Model):
    TIPO = (
        ("V", "Venda"),
        ("A", "Aluguel"),
    )
    codigo = models.CharField(max_length=10, unique=True, null=True, blank=True)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    tipo = models.CharField(max_length=1, choices=TIPO)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.FileField(upload_to="anuncios")
    usuario = models.ForeignKey("usuarios.CustomUser", on_delete=models.CASCADE)
    bike = models.ForeignKey("bikes.Bike", on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        if not self.codigo:
            self.codigo = get_random_string(16)
        super().save(*args, **kwargs)

class Chat(models.Model):
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
    comprador = models.ForeignKey("usuarios.CustomUser", on_delete=models.CASCADE)
    vendedor = models.ForeignKey("usuarios.CustomUser", on_delete=models.CASCADE, related_name="vendedor")
    last_message = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.anuncio.titulo
    
class Messages(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    message = models.TextField(default='[]')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
    
    def adicionar_mensagem(self, message):
        historico = json.loads(self.message)
        resposta = {
            'sender': message['sender'],
            'message': message['message'],
            'date': message['date'],
        }
        historico.append(resposta)
        Chat.objects.filter(id=self.chat.id).update(last_message=message['message'])
        self.message = json.dumps(historico)
        self.save()
        self.notificar_usuarios(message)

    def get_historico(self):
        historico = json.loads(self.message)
        return historico
    
    def notificar_usuarios(self, message):
        # TODO: Implementar notificação
        pass