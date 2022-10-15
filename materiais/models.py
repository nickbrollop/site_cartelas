from pyexpat import model
from django.db import models

# Create your models here.

class tipo_Material(models.Model):
    nome = models.CharField(max_length = 100)
    cod_tipo  = models.IntegerField
    descricao_tipo = models.CharField(max_length = 100)
    def __str__(self):
        return self.nome

class material(models.Model):
    cod_material = models.IntegerField
    nome = models.CharField(max_length = 50)
    parte_recicl = models.CharField(max_length = 20)
    descricao = models.CharField(max_length = 100)
    material_tipo_mat = models.ForeignKey(tipo_Material, on_delete=models.SET_NULL, null = True)
    def __str__(self):
        return self.nome