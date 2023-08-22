def formatador_cpf(user):
    if len(user.cpf) == 11:
        return f"{user.cpf[:3]}.{user.cpf[3:6]}.{user.cpf[6:9]}-{user.cpf[9:]}"


def save_user(form):
    user = form.save(commit=False)
    user.cpf = formatador_cpf(user)
    user.first_login = False
    user.save()
