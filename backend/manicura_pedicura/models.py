from django.db import models

class ManicuraPedicura(models.Model):
    nombre = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='manicura_pedicura/')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre