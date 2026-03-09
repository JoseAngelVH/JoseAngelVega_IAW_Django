from django.db import models
from app_secciones.models import Seccion

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    enlace = models.URLField(blank=True, null=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre