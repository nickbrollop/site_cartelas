from django.shortcuts import render
from enderecos.forms import doacoesForm
#from myapp.forms import ContactForm
from django.views import View
from django.views.generic.edit import FormView

from enderecos.models import loc_Entrega
# Create your views here.

class ContactFormview(FormView):
    template_name ='contato.html'
    #form_class = ContactForm
    success_url ="/Obrigada/"
    
class EnderecosView(View):
    template_name = 'doacao.html'
    form_class = doacoesForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        
        form = self.form_class(request.POST)
        print(form)
        cidade = self.form.cleaned_data['select_cidade']
        material = self.form.cleaned_data['select_material']
        
        locais = loc_Entrega.objects.filter(loc_Entrega_cidade = cidade)

        return render(request, self.template_name, {'form': form, 'enderecos':locais})
    

    

