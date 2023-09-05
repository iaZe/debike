from django import forms

from .models import CustomUser

class CustomUserCompleteForm(forms.ModelForm):
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
    first_name = forms.CharField(
        required=True,
        label="Nome",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    last_name = forms.CharField(
        required=True,
        label="Sobrenome",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    cpf = forms.CharField(
        required=True,
        label="CPF",
        min_length=11,
        max_length=14,
        widget=forms.TextInput(attrs={"class": "form-control", "pattern": "\d{3}\.\d{3}\.\d{3}-\d{2}", "placeholder": "000.000.000-00"}),
    )
    sexo = forms.ChoiceField(
        required=True,
        label="Sexo",
        choices=SEXO,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    telefone = forms.CharField(
        required=True,
        label="Telefone",
        min_length=11,
        max_length=14,
        widget=forms.TextInput(attrs={"class": "form-control", "pattern": "\(\d{2}\)\d{5}-\d{4}", "placeholder": "(00) 00000-0000"}),
    )
    data_nascimento = forms.DateField(
        required=True,
        label="Data de nascimento",
        widget=forms.DateInput(attrs={"class": "form-control"}),
    )
    cidade = forms.CharField(
        required=True,
        label="Cidade",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    estado = forms.ChoiceField(
        required=True,
        label="Estado",
        choices=ESTADO,
        widget=forms.Select(attrs={"class": "form-control"}),
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
