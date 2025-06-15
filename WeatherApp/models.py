from django.db import models
from django.db import models


class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    description = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.city} - {self.temperature}°C"