from django.shortcuts import render

from rest_framework import viewsets

from .serializers import TeamDataSerializer
from ITSP.models import TeamData

# Create your views here.

class TeamDataViewSet(viewsets.ModelViewSet):
    queryset = TeamData.objects.all().order_by('team_id')
    serializer_class = TeamDataSerializer

