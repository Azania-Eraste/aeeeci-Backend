from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=350)
    dateDebut = models.DateField(null=True)
    dateFin = models.DateField()
    delai = models.DateTimeField()
    participants = models.ManyToManyField("auth_app.ScoutUser", null=True)
    participation = models.IntegerField()