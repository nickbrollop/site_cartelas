from django.db import models

# Create your models here.

class loc_Entrega(models.Model):
    cod_ent = models.IntegerField
    local = models.CharField(50)
    tel = models.CharField(13)
    horario = models.TimeField()
    endereco = models.CharField(100)
    descricao_local = models.CharField(100)
    
class cidades(models.Model):
    cod_cid = models.IntegerField
    endereco = models.CharField(100)
    cep = models.CharField(8)
    descricao_cidade = models.CharField(100)