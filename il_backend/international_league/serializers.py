from rest_framework import serializers
from .models import *


class PilotSerializer(serializers.ModelSerializer):
    """
    Сериализатор пилотов
    """

    class Meta:
        model = Pilot
        fields = '__all__'
