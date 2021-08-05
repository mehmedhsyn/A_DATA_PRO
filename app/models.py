from django.db import models

# Create your models here.

class Allmatchs(models.Model):
    team1 = models.CharField(max_length=50)
    team2 = models.CharField(max_length=50)
    data = models.DateTimeField()

class Nextmatchs(models.Model):
    team1 = models.CharField(max_length=50)
    team2 = models.CharField(max_length=50)
    data = models.DateTimeField()

    
class WinLose(models.Model):
    Position = models.IntegerField()
    Name = models.CharField(max_length=50)
    Wins = models.IntegerField()
    Loses = models.IntegerField()
    Equal = models.IntegerField()
    Points = models.IntegerField()


    
    
