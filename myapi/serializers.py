# serializers.py
from rest_framework import serializers

from ITSP.models import TeamData

class TeamDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeamData
        fields = ('team_name', 'team_id', 'team_members')