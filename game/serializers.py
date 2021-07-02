from rest_framework.serializers import ModelSerializer, ValidationError
from .models import UserPlanetArmy


class UserPlanetArmySerializer(ModelSerializer):

    class Meta:
        model = UserPlanetArmy       # model to serialize
        fields = ['planet_name', 'army_name']  # How many fields to display ("__all__")
