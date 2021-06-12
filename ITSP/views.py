from django.shortcuts import render
from django.http import HttpResponse
from .models import TeamData

# Create your views here.

def userInfo(request, teamid):
        return render(request, 'ITSP/dynam.html', {'dbid' : TeamData.objects.filter(team_id = teamid)})

def index(request):
    return render(request, 'ITSP/index.html', {'data' : TeamData.objects.all()})
