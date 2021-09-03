from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action

from .models import *
from .serializers import *


class TeamListView(APIView):
    @staticmethod
    def get(request):
        teams = Team.objects.all().order_by('name')
        instances = TeamSerializer(teams, many=True).data
        return Response(instances)


class PilotListView(APIView):
    @staticmethod
    def get(request):
        pilots = Pilot.objects.filter(is_main_pilot=True).\
            order_by('league', '-total_score', 'best_race_finish', 'highest_grid_position')
        instances = PilotSerializer(pilots, many=True).data
        return Response(instances)


class TeamDetailView(APIView):
    @staticmethod
    def get(request, url_name):
        teams = Team.objects.get(url_name=url_name)
        instances = TeamSerializer(teams).data
        return Response(instances)


class RaceListView(APIView):
    @staticmethod
    def get(request):
        race = Race.objects.all().order_by('place_in_calendar')
        instances = RaceSerializer(race, many=True).data
        return Response(instances)


class RaceDetailView(APIView):
    @staticmethod
    def get(request, country):
        race = Race.objects.get(country=country)
        instances = RaceSerializer(race).data
        return Response(instances)
