from django.db import models

class SimulationData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()