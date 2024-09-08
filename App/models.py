from django.db import models

# Create your models here.
class Marca(models.Model):
    marcaId = models.CharField(primary_key= True, max_length= 3)
    marcaNombre = models.CharField(max_length= 20)
    
    def __str__(self):
        return "{}".format(self.marcaNombre)
    
class TipoVehiculo(models.Model):
    
    tipoVehiculoId = models.CharField(primary_key= True, max_length= 3)
    tipoVehiculo = models.CharField(max_length= 20)
    
    def __str__(self):
        return "{}".format(self.tipoVehiculo)
    
class Vehiculo(models.Model):
    
    idVehiculo = models.AutoField(primary_key= True)
    patente = models.CharField(max_length= 30)
    chasis = models.CharField(max_length= 30)
    motor = models.CharField(max_length= 30)
    modelo = models.CharField(max_length= 100)
    fechavencimiento = models.DateField()
    poseeseguro = models.BooleanField(default=False)
    observaciones = models.CharField(max_length=1000)
    
    tipoVehiculoId = models.ForeignKey(TipoVehiculo, null= True, blank= False, on_delete= models.RESTRICT)
    marcaId = models.ForeignKey(Marca, null= True, blank= False, on_delete= models.RESTRICT)