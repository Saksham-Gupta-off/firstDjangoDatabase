from django.db import models
import datetime

# Create your models here.
class TeamData(models.Model):
    team_name =  models.CharField(max_length=220)
    team_id = models.CharField(max_length=9, default="ITS200001")

    team_members = models.TextField(default="John Doe, Jane Doe")

    def __str__(self):
        return self.team_name
    