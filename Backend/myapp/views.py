from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def myhome(request):
    return render(request, 'index.html')

def agendamento(request):
    return render(request, 'agendamento/agendamento.html')

def agendamento_com_sucesso(request):
    return render(request, 'agendamento/sucesso.html')

@login_required
def perfil(request):
    return render(request, 'perfil.html')