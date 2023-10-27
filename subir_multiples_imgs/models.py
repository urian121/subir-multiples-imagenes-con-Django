from django.db import models

# Create your models here.


class Galeria(models.Model):
    # la palabra upload_to se utiliza para especificar la ubicación en la que se almacenarán los archivos cargados a través del campo models.ImageField
    images = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table = "imgs"
        ordering = ['-created_at']
