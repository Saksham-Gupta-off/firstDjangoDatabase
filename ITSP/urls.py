from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('../API', views.index, name='API'),
    path('<str:teamid>', views.userInfo, name='idpage')
]