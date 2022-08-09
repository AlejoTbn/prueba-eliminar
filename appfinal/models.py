from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50)    
    clave = models.CharField(max_length=50)  

class Conductor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    cedula = models.CharField(max_length=10,verbose_name='Cedula')
    telefono = models.CharField(max_length=10,verbose_name='Telefono')
    direccion = models.CharField(max_length=20,verbose_name='Direccion')
    ciudad = models.CharField(max_length=20,verbose_name='Ciudad')
    placa = models.ImageField(upload_to='imagenes/',verbose_name='Placa')


    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + "Cedula: " + self.cedula + " - " + "Cidad: " + self.ciudad
        return fila
        
    def delete(self, using=None, keep_parents= False):
        self.placa.storage.delete(self.placa.name)
        super().delete()