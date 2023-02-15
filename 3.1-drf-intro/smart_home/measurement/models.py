from django.db import models


class Sensor(models.Model):
    sensor_name = models.CharField(max_length=60)
    description = models.CharField(max_length=60, default=None)


class Measurement(models.Model):
    sensor = models.ForeignKey(
        Sensor, related_name='sensor', on_delete=models.CASCADE)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(max_length=60, null=True)
