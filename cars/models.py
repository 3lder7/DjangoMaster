from django.db import models  # type: ignore[import-not-found, reportMissingImports]

class Car(models.Model):#tabela Car no banco que herda a classe Model já imbutida no django
    id = models.AutoField(primary_key=True)#AutoField vem de Model (auto incremental)
    model = models.CharField(max_length=200)#CharField vem de Model (campo de texto)
    brand = models.CharField(max_length=200)
    factory_year = models.IntegerField(blank=True, null=True)#IntegerField vem de Model (Campo de valor inteiro)
    model_year =  models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)#FloatField vem de Model (Campo de valor flutuante)