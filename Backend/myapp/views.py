from django.shortcuts import render, redirect
from .forms import AgendamentoForm
from django.contrib.auth.decorators import login_required

from django.conf import settings 
from django.template.loader import get_template  
from django.core.mail import EmailMessage 
from django.contrib.auth.forms import UserCreationForm

def sendmail_agendamento(data):
    message_body = get_template('agendamento/enviar.html').render(data)  
    email = EmailMessage('Formulário de Agendamento', 
                            message_body, settings.DEFAULT_FROM_EMAIL,
                            to=['abracamente.contato@gmail.com'])
    email.content_subtype = "html"    
    return email.send()

# Create your views here.
def myhome(request):
    return render(request, 'index.html')

def tipo_agendamento(request):
    return render(request, 'agendamento/tipo_agendamento.html')

def agendamento(request):

    if request.method == 'POST':
        form = AgendamentoForm(request.POST) 
        if form.is_valid():
            form = form.save(commit=False)
            form.save()

            data = { 
                'name': request.POST.get('name'), 
                'phone': request.POST.get('phone'),
                'age': request.POST.get('age'),
                'email': request.POST.get('email'),
                'gender': request.POST.get('gender'),
                'mode': request.POST.get('mode'),
                'date': request.POST.get('date'),
                'hour': request.POST.get('hour'),
                'message': request.POST.get('message'),
            }
            
            sendmail_agendamento(data)


            return redirect('agendamento_com_sucesso')
    else:
        form = AgendamentoForm()

    return render(request, 'agendamento/agendamento.html', {'form': form})

def agendamento_com_sucesso(request):
    return render(request, 'agendamento/sucesso.html')

@login_required
def perfil(request):
    return render(request, 'perfil.html')

def connect(request):
    form = UserCreationForm()
    return render(request, 'registration/connect.html', {'form': form})
