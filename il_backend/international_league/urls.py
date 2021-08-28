from django.urls import path

from international_league.views import PilotView

urlpatterns = [
    path('pilots/', PilotView.as_view())
]
