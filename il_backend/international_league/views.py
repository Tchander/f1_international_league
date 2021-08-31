from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action

from .models import *
from .serializers import *


class TeamView(APIView):
    @staticmethod
    def get(request):
        teams = Team.objects.all().order_by('name')
        instances = TeamSerializer(teams, many=True).data
        return Response(instances)


class PilotView(APIView):
    @staticmethod
    def get(request):
        pilots = Pilot.objects.all().order_by('league')
        instances = PilotSerializer(pilots, many=True).data
        return Response(instances)


class TeamDetailView(APIView):
    @staticmethod
    def get(request, url_name):
        teams = Team.objects.get(url_name=url_name)
        instances = TeamSerializer(teams).data
        return Response(instances)
