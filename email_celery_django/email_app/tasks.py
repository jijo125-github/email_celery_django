from celery import shared_task
from time import sleep
from email_celery_django.email_conf import EMAIL_HOST_USER, RECEPIENT

@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def send_email_task():
    sleep(20)
    subject = 'Email Testing via Celery'
    message = 'Hello user, how are you?'
    recepeint = RECEPIENT
    send_mail(subject, message, EMAIL_HOST_USER, recepient, fail_silently=False)
    return None
