from django.shortcuts import render
from enderecos.forms import doacoesForm, ContatoForm
from django.views import View
from django.views.generic.edit import FormView

from enderecos.models import contato, loc_Entrega
# Create your views here.

class ContactFormview(FormView):
    template_name ='contato.html'
    #form_class = ContactForm
    success_url ="/contato/"
    
class EnderecosView(View):
    template_name = 'doacao.html'
    form_class = doacoesForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        #import ipdb; ipdb.set_trace()
        form = self.form_class(request.POST)
        
        if form.is_valid():
            cidade = form.cleaned_data['select_cidade']
            material = form.cleaned_data['select_material']
        
            locais = loc_Entrega.objects.filter(loc_Entrega_cidade = cidade)

        return render(request, self.template_name, {'form': form, 'enderecos': locais})


class ContatoView(View):
    template_name = 'contato.html'
    form_class = ContatoForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        #import ipdb; ipdb.set_trace()
        form = self.form_class(request.POST)
        
        if form.is_valid():
            contato.objects.create(form)

        return render(request, self.template_name, {'form': form})
'''def contact(request):
	if request.method == 'POST':
		form = contatoForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("main:homepage")
      
	form = ContactForm()
	return render(request, "main/contact.html", {'form':form})'''
    

    

