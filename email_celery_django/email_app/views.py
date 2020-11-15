from django.shortcuts import render
from django.http import HttpResponse
from .tasks import sleepy, send_email_task

# Create your views here.

def index(request):
    sleepy.delay(15)
    return HttpResponse('Took 15 seconds to load..')

def send_mail(request):
    send_email_task.delay()
    return HttpResponse('Mail has been sent via celery..')



