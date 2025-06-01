from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm, ConnectForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def connect(request):
        if request.method == "POST":
            form = ConnectForm(request.POST)
            login_form = LoginForm()
    
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, 'Registrado com sucesso!')
                return redirect('perfil')

            else:
                messages.error(request, 'Corrija os erros abaixo.')
        else:
            form = ConnectForm()
            login_form = LoginForm()
        return render(request, 'registration/connect.html', {
            'form': form,
            'login_form': login_form,
            'show_login': True if request.method == "POST" and not login_form.is_valid() else False
            })
        
def login_view(request):
    if request.method == "POST":
        login_form = LoginForm(request, data=request.POST)
        form = ConnectForm()
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('perfil')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
            show_login = True
    else:
        form = ConnectForm()
        login_form = LoginForm()
        show_login = True
    return render(request, 'registration/connect.html', {
        'form': form,
        'login_form': login_form,
        'show_login': False if request.method == "POST" else True
        }) 
