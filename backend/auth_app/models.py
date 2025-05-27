from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):

    isScout = models.BooleanField(default=False)
    number = models.CharField(max_length=250)

    def promote_to_scout(self, scoutID):
        if self.isScout and not hasattr(self, 'ScoutUser'):
            ScoutUser.objects.create(
                a_ptr=self,
                scoutID=scoutID
            )


class ScoutUser(CustomUser):
    scoutID = models.CharField(max_length=250, unique=True)