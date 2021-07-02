from django.db import models
from django.contrib.auth.models import User


class UserPlanetArmy(models.Model):
    # If blank=True, the field is allowed to be blank
    # if null=True, Django will store empty values as NULL in the database

    # ForeignKey to define a many-to-one relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    planet_name = models.CharField(max_length=20)
    army_name = models.CharField(max_length=20)


    def __str__(self):
        return str(self.user)
