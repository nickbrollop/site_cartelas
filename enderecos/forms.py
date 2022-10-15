from django import forms
from materiais.models import material
from enderecos.models import cidades

class doacoesForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    select_material = forms.ModelChoiceField(queryset = material.objects.all(), empty_label="Selecione o material desejado...")
    select_cidade = forms.ModelChoiceField(queryset = cidades.objects.all(), empty_label="Selecione a cidade desejada...")
