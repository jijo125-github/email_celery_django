from django.urls import path
from email_app import views

urlpatterns = [
    path('', views.index, name = 'index'),
]