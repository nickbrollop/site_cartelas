from django import forms
from materiais.models import material
from enderecos.models import cidades

class doacoesForm(forms.Form):
    select_material = forms.ModelChoiceField(queryset = material.objects.all(), empty_label = "Selecione o material desejado...", label="")
    select_cidade = forms.ModelChoiceField(queryset = cidades.objects.all(), empty_label = "Selecione a cidade desejada...", label="")
