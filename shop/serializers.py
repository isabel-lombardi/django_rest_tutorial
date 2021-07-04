from rest_framework.serializers import ModelSerializer
from .models import UserTroop


class UserTroopSerializer(ModelSerializer):

    class Meta:
        model = UserTroop       # model to serialize

        # ['troop_id', 'troop_name', 'troop_level', 'troop_att', 'troop_def']
        fields = ['troop_id']  # How many fields to display ("__all__")
