from django import forms
from materiais.models import material
from enderecos.models import cidades, contato
from django.forms import ModelForm


class doacoesForm(forms.Form):
    select_material = forms.ModelChoiceField(queryset = material.objects.all(), empty_label = "Selecione o material desejado...", label="")
    select_cidade = forms.ModelChoiceField(queryset = cidades.objects.all(), empty_label = "Selecione a cidade desejada...", label="")

class ContatoForm(ModelForm):
    class Meta:
        model = contato
        fields = ['nome', 'telefone', 'email', 'cidade', 'mensagem']

'''class contatoForm(forms.Form):
    select_material = forms.ModelChoiceField(, empty_label = "Selecione o material desejado...", label="")
    select_cidade = forms.ModelChoiceField(queryset = cidades.objects.all(), empty_label = "Selecione a cidade desejada...", label="")'''