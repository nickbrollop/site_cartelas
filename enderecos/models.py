from django.db import models

# Create your models here.

class loc_Entrega(models.Model):
    cod_ent = models.IntegerField
    local = models.CharField(max_length = 50)
    tel = models.CharField(max_length = 13)
    horario = models.TimeField()
    endereco = models.CharField(max_length = 100)
    descricao_local = models.CharField(max_length = 100)
    def __srt__(self):
        return self.endereço
    
class cidades(models.Model):
    cod_cid = models.IntegerField
    cidade = models.CharField(max_length = 100)
    descricao_cidade = models.CharField(max_length = 100)
    def __srt__(self):
        return self.cidade