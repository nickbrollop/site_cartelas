from django.db import models

# Create your models here.

class material(models.Model):
    cod_material = models.IntegerField
    parte_recicl = models.CharField(20)
    descricao = models.CharField(100)

class tipo_Material(models.Model):
    cod_tipo  = models.IntegerField
    descricao_tipo = models.CharField(100)
    