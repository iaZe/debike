from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    SEXO = (
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("O", "Outro"),
        ("N", "Prefiro não informar"),
    )
    ESTADO = (
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins"),
    )
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO, null=True, blank=True)
    telefone = models.CharField(max_length=11, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=2, choices=ESTADO, null=True, blank=True)
    first_login = models.BooleanField(default=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)
