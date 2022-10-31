from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from enderecos.views import EnderecosView, ContatoView
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path("accounts/",include("django.contrib.auth.urls")),
    path ('RecandoDaCompaixao/PaginaInicial/', TemplateView.as_view( template_name ='home_page.html'), name = 'pagina_inicial' ),
    path ('RecandoDaCompaixao/QuemSomos/', TemplateView.as_view( template_name ='quem_somos.html'), name = 'quem_somos'),
    path ('RecandoDaCompaixao/Contato/', ContatoView.as_view(), name = 'contato' ),
    path ('RecandoDaCompaixao/Informacional/', TemplateView.as_view( template_name ='informacional.html'), name = 'informacional' ),
    path ('RecandoDaCompaixao/Doacao/', EnderecosView.as_view(), name = 'doacao' ),
]


