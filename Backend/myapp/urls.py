from django.urls import path 
from myapp import views

urlpatterns = [
    path('', views.myhome, name='myhome'),
    path('tipo-agendamento/', views.tipo_agendamento, name="tipo_agendamento"),
    path('agendamento/', views.agendamento, name='agendamento'),
    path('agendamento_com_sucesso/', views.agendamento_com_sucesso, name='agendamento_com_sucesso'),
    path('perfil/', views.perfil, name='perfil'),
]