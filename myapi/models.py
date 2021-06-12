from django.db import models

# Create your models here.
class TeamData(models.Model):
    team_name =  models.CharField(max_length=220)
    team_id = models.CharField(max_length=9, default="ITS200001", primary_key=True)

    team_members = models.TextField(default="John Doe, Jane Doe")

    def __str__(self):
        return f'{self.team_id} - {self.team_name} - {self.team_members}'
    
