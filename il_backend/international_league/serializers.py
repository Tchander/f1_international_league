from rest_framework import serializers
from .models import *


class TeamSerializer(serializers.ModelSerializer):
    """
    Сериализатор команд
    """
    pilots = serializers.SerializerMethodField()

    @staticmethod
    def get_pilots(obj):
        return PilotSerializer(Pilot.objects.filter(team_id=obj.id), many=True).data

    class Meta:
        model = Team
        fields = '__all__'


class PilotSerializer(serializers.ModelSerializer):
    """
    Сериализатор пилотов
    """

    class Meta:
        model = Pilot
        fields = '__all__'
