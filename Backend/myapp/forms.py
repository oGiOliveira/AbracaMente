from django import forms
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    GENDER_CHOICES = [
         ('', 'Selecione'),
         ('masculino', 'Masculino'),
         ('feminino', 'Feminino'),
         ('outro', 'Outro'),
    ]
    MODE_CHOICES = [
         ('', 'Selecione'),
         ('presencial', 'Presencial'),
         ('online', 'Online'),
    ]
    DATE_CHOICES = [
         ('24/05/2025', '24/05/2025'),
         ('31/05/2025', '31/05/2025'),
         ('07/06/2025', '07/06/2025'),
    ]
    HOUR_CHOICES = [
         ('19:00', '19:00'),
         ('20:00', '20:00'),
         ('21:00', '21:00'),
    ]
    
    name = forms.CharField(label='Nome Completo')
    phone = forms.CharField(label='Telefone')
    email = forms.EmailField(label='Email')
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Gênero', widget=forms.Select(attrs={'id': 'genero', 'class': 'form-control'}))
    mode = forms.ChoiceField(choices=MODE_CHOICES, label='Modalidade', widget=forms.Select(attrs={'id': 'modalidade', 'class': 'form-control'}))
    date = forms.ChoiceField(choices=DATE_CHOICES, widget=forms.RadioSelect, label='Datas Disponíveis')
    hour = forms.ChoiceField(choices=HOUR_CHOICES, widget=forms.RadioSelect, label='Horários Disponíveis')
    message = forms.CharField(label='Deixe uma mensagem sobre o motivo do agendamento e/ou que tipo de profissional você procura', widget=forms.Textarea)

    class Meta:
        model = Agendamento
        fields = ['name', 'phone', 'age', 'email', 'gender', 'mode', 'date', 'hour', 'message'] 
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
              if field_name not in ['date', 'hour']:
               field.widget.attrs['class'] = 'form-control'
              