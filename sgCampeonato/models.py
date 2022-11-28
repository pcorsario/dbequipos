from django.db import models

# Create your models here.

class Player(models.Model):
    name=models.CharField(max_length=100)
    number=models.IntegerField()
    rc=models.IntegerField()
    yc=models.IntegerField()
    goals=models.IntegerField()
    assists=models.IntegerField()
    def __str__(self):
        return self.name

class Team(models.Model):
    country=models.CharField(max_length=100)
    course=models.CharField(max_length=50)
    mp=models.IntegerField()
    points=models.IntegerField()