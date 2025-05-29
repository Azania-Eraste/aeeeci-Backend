from django.db import models
from enum import Enum

# Create your models here.
class TypeEvent(Enum):
    FORMATION = "Formation"
    AG = "Assemblée Générale"
    JAMBOREE = "Jamborée"
    RENTREE_SCOUTE = "Rentrée scoute"


class Event(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=350)
    dateDebut = models.DateField(null=True)
    dateFin = models.DateField()
    delai = models.DateTimeField()
    participants = models.ManyToManyField("auth_app.ScoutUser")
    participation = models.IntegerField()
    type = models.CharField(max_length=50, choices=[(tag.name, tag.value) for tag in TypeEvent], null=True)