from django.db import models

# Create your models here.

class Producto(models.Model):
    """
    Tabla producto para el registro en la base de datos
    """
    nombre = models.CharField("Nombre Producto", max_length=70)
    descripcion = models.CharField("Descripcion", max_length=200)
    precio = models.FloatField()
    stock  = models.IntegerField("Cantidad disponible")
    imagen = models.ImageField(upload_to='imagenes/', default=None, verbose_name="Imagen")
    
    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
