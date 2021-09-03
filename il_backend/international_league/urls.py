from django.urls import path

from international_league.views import *

urlpatterns = [
    path('teams/<str:url_name>/', TeamDetailView.as_view()),
    path('races/<str:country>/', RaceDetailView.as_view()),
    path('teams/', TeamListView.as_view()),
    path('pilots/', PilotListView.as_view()),
    path('races/', RaceListView.as_view()),
]
