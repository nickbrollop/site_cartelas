from django.db import models

# Create your models here.

class cidades(models.Model):
    cod_cid = models.IntegerField
    cidade = models.CharField(max_length = 100)
    descricao_cidade = models.CharField(max_length = 100)
    def __str__(self):
        return self.cidade
    
class loc_Entrega(models.Model):
    cod_ent = models.IntegerField
    local = models.CharField(max_length = 50)
    tel = models.CharField(max_length = 13)
    horario = models.TimeField()
    endereco = models.CharField(max_length = 100)
    descricao_local = models.CharField(max_length = 100)
    loc_Entrega_cidade = models.ForeignKey(cidades, on_delete=models.SET_NULL, null = True)
    def __str__(self):
        return self.local
    
class contato(models.Model):
    nome = models.CharField(max_length = 50)
    telefone = models.CharField(max_length = 13)
    email = models.EmailField
    cidade = models.CharField(max_length = 100)
    mensagem = models.TextField
    def __str__(self):
        return self.nome