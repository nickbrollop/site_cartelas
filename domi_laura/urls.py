from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from enderecos.views import EnderecosView, ContatoView
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path("accounts/",include("django.contrib.auth.urls")),
    path ('RecantoDaCompaixao/PaginaInicial/', TemplateView.as_view (template_name ='home_page.html'), name = 'pagina_inicial' ),
    path ('RecantoDaCompaixao/QuemSomos/', TemplateView.as_view (template_name ='quem_somos.html'), name = 'quem_somos'),
    path ('RecantoDaCompaixao/Contato/', ContatoView.as_view(), name = 'contato' ),
    path ('RecantoDaCompaixao/Informacional/', TemplateView.as_view (template_name ='informacional.html'), name = 'informacional' ),
    path ('RecantoDaCompaixao/Doacao/', EnderecosView.as_view(), name = 'doacao' ),
]