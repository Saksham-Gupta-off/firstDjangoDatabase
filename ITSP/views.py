from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello there")
def index1(request):
    return HttpResponse("Hello a there")