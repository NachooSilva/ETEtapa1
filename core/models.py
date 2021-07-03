from django.db import models

# Create your models here.
class Colaborador(models.Model):   

    rutColaborador =  models.CharField(primary_key=True,max_length=10, verbose_name='Rut de Colaborador')
    image = models.ImageField(upload_to='img',verbose_name='Imagen')
    nombre = models.CharField(max_length=100,verbose_name='Nombre completo')
    telefono = models.IntegerField(verbose_name='Telefono')
    direccion = models.CharField(max_length=100, verbose_name='Direccion')
    correo = models.CharField(max_length=50, verbose_name='Correo')
    pais = models.CharField(max_length=50, verbose_name='pais')
    contraseña = models.CharField(max_length=30, verbose_name='contraseña')

    def __str__(self):
        return self.rutColaborador