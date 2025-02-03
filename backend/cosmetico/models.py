from django.db import models

class Cosmetico(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='cosmeticos/')
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre