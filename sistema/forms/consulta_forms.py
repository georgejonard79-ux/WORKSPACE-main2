from django import forms
from sistema.models import Consulta

class ConsultaForm(forms.ModelForm):
    # Troca o Charfield padrão por um <select> com opções fixas
    cpf = forms.CharField(
        label='CPF',
        max_length=14,
        help_text='Pode digitar com ou sem pontos e traços.',
        widget=forms.TextInput(attrs={'placeholder': '123.456.789-01', 'inputmode': 'numeric'}),
    )
    
    class Meta:
        model = Paciente
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'cpf', 'imagem',]
        # criacao_data e ativo não aparecem: são preenchidos automaticamente.
        labels = {
            'nome': 'Nome',
            'sobrenome': 'Sobrenome',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'cpf': 'CPF',
        }
        
