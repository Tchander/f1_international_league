from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action

from .models import *
from .serializers import *


class PilotView(APIView):
    @staticmethod
    def get(request):
        pilots = Pilot.objects.all()
        instances = PilotSerializer(pilots, many=True).data
        return Response(instances)
