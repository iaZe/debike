from django import forms
from .models import Bike, Venda


class CadastrarBikeForm(forms.ModelForm):
    codigo = forms.CharField(
        required=True,
        label="Código",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    modelo = forms.CharField(
        required=True,
        label="Modelo",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    cor = forms.CharField(
        required=True,
        label="Cor",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    foto = forms.FileField(
        required=False,
        label="Fotos",
        widget=forms.ClearableFileInput(attrs={"multiple": False, "class": "form-control"}),
    )

    class Meta:
        model = Bike
        fields = ["codigo", "modelo", "cor", "foto"]


class ConsultarBikeForm(forms.Form):
    codigo = forms.CharField(
        required=True,
        label="Código",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        fields = ["codigo"]

class VenderBikeForm(forms.ModelForm):
    cpf = forms.CharField(
        required=True,
        label="CPF do comprador",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    valor = forms.CharField(
        required=True,
        label="Valor",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Venda
        fields = ["cpf", "valor"]
        