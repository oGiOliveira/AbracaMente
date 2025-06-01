from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class ConnectForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Nome de usuário"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
            "password1": forms.PasswordInput(attrs={"placeholder": "Senha"}),
            "password2": forms.PasswordInput(attrs={"placeholder": "Confirme a senha"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirme a senha'
        
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Email ou usúario'
        self.fields['password'].widget.attrs['placeholder'] = 'Senha'