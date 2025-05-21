from django.urls import path 
from myapp import views

urlpatterns = [
    path('', views.myhome, name='myhome'),
    path('agendamento/', views.agendamento, name='agendamento'),
    path('agendamento_com_sucesso/', views.agendamento_com_sucesso, name='agendamento_com_sucesso'),
    path('perfil/', views.perfil, name='perfil'),
]