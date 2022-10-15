from pyexpat import model
from django.db import models

# Create your models here.

class material(models.Model):
    cod_material = models.IntegerField
    parte_recicl = models.CharField(max_length = 20)
    descricao = models.CharField(max_length = 100)

class tipo_Material(models.Model):
    nome = models.CharField(max_length = 100)
    cod_tipo  = models.IntegerField
    descricao_tipo = models.CharField(max_length = 100)
    