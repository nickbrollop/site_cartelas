from myapp.forms import ContactForm
from django.views import View
from django.views.generic.edit import FormView
# Create your views here.

class ContactFormview(FormView):
    template_name ='contato.html'
    form_class = ContactForm
    success_url ="/Obrigada/"
    
class EnderecosView(View):
    template_name = 'form_template.html'
    

