from django.urls import path
from email_app import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('email/', views.send_mail, name = 'mail')
]