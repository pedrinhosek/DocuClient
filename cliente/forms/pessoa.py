from django import forms
from django.core.exceptions import ValidationError
from cliente.models import Pessoa
from cliente.utils import cpf_verification, cnpj_verification


class PessoaForm(forms.ModelForm):

    def clean_cpf(self):
        numero = self.cleaned_data['cpf'].replace('.', '').replace('-', '').replace('/', '')
        
        if len(numero) == 11 and not cpf_verification(numero):    
            raise ValidationError('CPF inválido')

        if len(numero) == 14 and cnpj_verification(numero):
            raise ValidationError('CNPJ inválido')

        return numero

    class Meta:
        model = Pessoa
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo', 'aria-describedby': 'id_nomeHelpBlock'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control cpf', 'placeholder': '000.000.000-00', 'aria-describedby': 'id_cpfHelpBlock'}),
            'fone': forms.TextInput(attrs={'class': 'form-control phone', 'placeholder': '(00) 00000-0000', 'aria-describedby': 'id_foneHelpBlock'}),
        }

        fields = [
            'nome',
            'cpf',
            'fone',
        ]
