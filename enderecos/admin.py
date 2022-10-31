from ast import Return
from django.contrib import admin
from enderecos.models import cidades, contato, loc_Entrega
# Register your models here.

admin.site.register(cidades)
admin.site.register(loc_Entrega)
admin.site.register(contato)
  