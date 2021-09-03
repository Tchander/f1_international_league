from rest_framework import serializers
from .models import *


class TeamSerializer(serializers.ModelSerializer):
    """
    Сериализатор команд
    """
    pilots = serializers.SerializerMethodField()

    @staticmethod
    def get_pilots(obj):
        return PilotSerializer(Pilot.objects.filter(team_id=obj.id, is_main_pilot=True), many=True).data

    class Meta:
        model = Team
        fields = '__all__'


class PilotSerializer(serializers.ModelSerializer):
    """
    Сериализатор пилотов
    """
    results = serializers.SerializerMethodField()
    team = serializers.SlugRelatedField(read_only=True, slug_field='name')

    @staticmethod
    def get_results(obj):
        return ResultSerializer(Result.objects.filter(pilot_id=obj.id, is_result_of_reserve_pilot=False)
                                .order_by('race_id'), many=True).data

    class Meta:
        model = Pilot
        fields = '__all__'


class RaceSerializer(serializers.ModelSerializer):
    """
    Сериализатор гонок
    """
    results = serializers.SerializerMethodField()

    @staticmethod
    def get_results(obj):
        return ResultSerializer(Result.objects.filter(race_id=obj.id), many=True).data

    class Meta:
        model = Race
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    """
    Сериализатор результатов
    """
    pilot = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Result
        fields = '__all__'
