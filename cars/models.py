from django.db import models  # type: ignore[import-not-found, reportMissingImports]

class Brand(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name #Corrige ortagrafia de 'Brand object' - retornando o nome do próprio modelo do carro

class Car(models.Model):#tabela Car no banco que herda a classe Model já imbutida no django
    id = models.AutoField(primary_key=True)#AutoField vem de Model (auto incremental)
    model = models.CharField(max_length=200)#CharField vem de Model (campo de texto)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name = 'car_brand')
    factory_year = models.IntegerField(blank=True, null=True)#IntegerField vem de Model (Campo de valor inteiro)
    model_year =  models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)#FloatField vem de Model (Campo de valor flutuante)
    plate = models.CharField(max_length=10, blank=True, null=True)#Placa do carro
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)#Foto do carro

    def __str__(self):
        return self.model 