from django import forms

from .models import CustomUser

class CustomUserCompleteForm(forms.ModelForm):
    SEXO = (
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("O", "Outro"),
        ("N", "Prefiro não informar"),
    )
    first_name = forms.CharField(
        required=True,
        label="Nome*",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    last_name = forms.CharField(
        required=True,
        label="Sobrenome*",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    cpf = forms.CharField(
        required=True,
        label="CPF*",
        min_length=11,
        max_length=11,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    sexo = forms.ChoiceField(
        required=True,
        label="Sexo*",
        choices=SEXO,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    telefone = forms.CharField(
        required=True,
        label="Telefone*",
        min_length=11,
        max_length=11,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    data_nascimento = forms.DateField(
        required=True,
        label="Data de nascimento*",
        widget=forms.DateInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "cpf",
            "sexo",
            "telefone",
            "data_nascimento",
            "cidade",
            "estado",
        ]


# class CustomUserUpdateForm(forms.ModelForm):
# TODO: Criar formulário de atualização de dados do usuário
