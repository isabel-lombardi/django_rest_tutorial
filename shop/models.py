from django.db import models
from django.contrib.auth.models import User


class UserTroop(models.Model):
    # If blank=True, the field is allowed to be blank
    # if null=True, Django will store empty values as NULL in the database

    # ForeignKey to define a many-to-one relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    troop_id = models.IntegerField()
    troop_name = models.CharField(max_length=20, default='')
    troop_level = models.IntegerField()
    troop_att = models.IntegerField()
    troop_def = models.IntegerField()



    def __str__(self):
        return str(self.user)