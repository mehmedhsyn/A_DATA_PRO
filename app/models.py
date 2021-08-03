from django.db import models

# Create your models here.

class Allmatchs(models.Model):
    team1 = models.CharField(max_length=50)
    team2 = models.CharField(max_length=50)
    data = models.DateTimeField()
    
