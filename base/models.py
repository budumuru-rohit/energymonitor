from django.db import models

class energymonitor(models.Model):
    current_r=models.DecimalField(max_digits=5, decimal_places=2)
    current_y=models.DecimalField(max_digits=5, decimal_places=2)
    current_b=models.DecimalField(max_digits=5, decimal_places=2)
    voltage_r=models.DecimalField(max_digits=5, decimal_places=2)
    voltage_y=models.DecimalField(max_digits=5, decimal_places=2)
    voltage_b=models.DecimalField(max_digits=5, decimal_places=2)
    avg_current=models.DecimalField(max_digits=5, decimal_places=2)
    avg_voltage=models.DecimalField(max_digits=5, decimal_places=2)
    power=models.DecimalField(max_digits=5, decimal_places=2)
    day=models.PositiveIntegerField(default=0)
    month=models.PositiveIntegerField(default=0)
    year=models.PositiveIntegerField(default=0)
    hour=models.PositiveIntegerField(default=0)
    minute=models.PositiveIntegerField(default=0)
    second=models.PositiveIntegerField(default=0)
    microsecond=models.PositiveIntegerField(default=0)

# Create your models here.
