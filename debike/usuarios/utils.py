from django.contrib import messages

from debike.settings import BASE_DIR
import re
import json

from .models import CustomUser

def save_user(form):
    user = form.save(commit=False)
    user.first_login = False
    user.save()

def validate_email(request, email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, email):
        user_exists = CustomUser.objects.filter(email=email).exists()
        if user_exists:
            return messages.error(request, "Usuário já cadastrado")
        email = email.lower()
        return email
    else:
        return messages.error(request, "E-mail inválido")


def validate_password(request, password, confirm_password):
    if password != confirm_password:
        return messages.error(request, "Senhas não conferem")
    
    if len(password) < 8:
        return messages.error(request, "Senha deve conter no mínimo 8 caracteres")
    
    if password.isdigit() or password.isalpha():
        return messages.error(request, "Senha deve conter letras e números")
    
    if password.islower() or password.isupper():
        return messages.error(request, "Senha deve conter letras maiúsculas e minúsculas")
    return True

def validate_cpf(request, cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    cpf_exists = CustomUser.objects.filter(cpf=cpf).exists()
    if cpf_exists:
        return messages.error(request, "CPF já cadastrado")

    if len(cpf) != 11:
        return messages.error(request, "Tamanho do CPF inválido")

    total = 0
    for i in range(9):
        total += int(cpf[i]) * (10 - i)
    resto = total % 11
    digito1 = 11 - resto if resto >= 2 else 0

    total = 0
    for i in range(10):
        total += int(cpf[i]) * (11 - i)
    resto = total % 11
    digito2 = 11 - resto if resto >= 2 else 0

    if not cpf[-2:] == f"{digito1}{digito2}":
        return messages.error(request, "CPF inválido")

    return cpf[-2:] == f"{digito1}{digito2}"

def validate_telefone(request, telefone):
    telefone = ''.join(filter(str.isdigit, telefone))

    if len(telefone) != 11:
        return messages.error(request, "Telefone inválido")
    
    if telefone[2] != "9":
        return messages.error(request, "Telefone deve conter o 9° dígito")
    
    path = BASE_DIR / "usuarios" / "DDD.json"
    with open(path, 'r') as json_file:
        ddd_estados = json.load(json_file)
    ddd = telefone[:2]
    estado = ddd_estados["DDD"].get(ddd)
    if not estado:
        return messages.error(request, "DDD inválido")
    return True