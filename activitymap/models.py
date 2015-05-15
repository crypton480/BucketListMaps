from django.db import models

# Create your models here.

class Marker(models.Model):
    user = models.CharField(max_length = 50)
    locationName = models.CharField(max_length = 50)
    text = models.CharField(max_length = 1024)
    time = models.DateTimeField()
    lat = models.DecimalField(max_digits=64, decimal_places=6)    
    lon = models.DecimalField(max_digits=64, decimal_places=6)

    def __str__(self):
        return self.text

