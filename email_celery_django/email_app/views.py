from django.shortcuts import render
from django.http import HttpResponse
from .tasks import sleepy

# Create your views here.

def index(request):
    sleepy.delay(15)
    return HttpResponse('Took 15 seconds to load..')



