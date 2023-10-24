from django import forms
from django.core.exceptions import ValidationError
from cliente.models import Pessoa
from cliente.utils import cpf_verification, cnpj_verification, ddd_brasil
CHOICE_SIM_NAO = (
    (True, 'SIM'),
    (False, 'NÃO'),
)


class PessoaForm(forms.ModelForm):

    def clean_nome(self):
        return self.cleaned_data.get('nome').upper()

    def clean_fone(self):
        fone = self.cleaned_data.get('fone').replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
        if not len(fone) == 11:
            raise ValidationError('Telefone inválido')
        if not int(fone[:2]) in ddd_brasil():
            raise ValidationError('O DDD informado não é válido')
        return fone

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
            'contrato_enviado': forms.RadioSelect(attrs={'class': 'form-check-input', 'type': 'radio'}, choices=CHOICE_SIM_NAO),
        }

        fields = [
            'nome',
            'cpf',
            'fone',
            'contrato_enviado',
        ]
