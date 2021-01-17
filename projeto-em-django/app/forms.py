from django.forms import ModelForm
from app.models import Pessoa

# Create the form class.
class PessoaForm(ModelForm):
     class Meta:
         model = Pessoa
         fields = ['nome', 'sobrenome', 'apelido', 'idade', 'data_de_nascimento', 'email', 'observacao']




