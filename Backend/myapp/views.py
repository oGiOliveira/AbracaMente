from django.shortcuts import render

# Create your views here.
def myhome(request):
    return render(request, 'index.html')

def agendamento(request):
    return render(request, 'agendamento/agendamento.html')

def agendamento_com_sucesso(request):
    return render(request, 'agendamento/sucesso.html')