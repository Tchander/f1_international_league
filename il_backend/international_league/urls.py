from django.urls import path

from international_league.views import *

urlpatterns = [
    path('teams/<str:url_name>/', TeamDetailView.as_view()),
    path('teams/', TeamView.as_view()),
    path('pilots/', PilotView.as_view()),
]
