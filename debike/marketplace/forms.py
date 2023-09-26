from django import forms

from .models import Anuncio

class AnuncioForm(forms.ModelForm):
    TIPO = (
        ("V", "Venda"),
        ("A", "Aluguel"),
    )
    titulo = forms.CharField(
        required=True,
        label="Título",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    descricao = forms.CharField(
        required=True,
        label="Descrição",
        widget=forms.Textarea(attrs={"class": "form-control"}),
    )
    tipo = forms.ChoiceField(
        required=True,
        label="Tipo",
        choices=TIPO,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    valor = forms.DecimalField(
        required=True,
        label="Valor",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
    foto = forms.FileField(
        required=False,
        label="Fotos",
        widget=forms.ClearableFileInput(attrs={"multiple": False, "class": "form-control"}),
    )
    class Meta:
        model = Anuncio
        fields = ["titulo", "descricao", "tipo", "valor", "foto"]