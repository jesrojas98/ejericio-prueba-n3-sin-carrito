from django.db import models

# Create your models here.
class productos(models.Model):   
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=150, blank=False, null=True)
    precio = models.CharField(max_length=50)

    def __str__(self):
        return str(self.nombre)
