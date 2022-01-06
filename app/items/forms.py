from django import forms
from django.forms import fields
from .models import Beneficiario
from .models import Medico
from .models import Especialidade
from .models import Procedimento
from .models import LocalAtendimento
from .models import Atendimento


class BeneficiarioForm(forms.ModelForm):
    class Meta:
        model = Beneficiario
        fields = ['nomeBeneficiario', 'datanascBeneficiario', 'sexoBeneficiario']

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nomeMedico', 'crm', 'datanascMedico', 'especialidade']

class EspecialidadeForm(forms.ModelForm):
    class Meta:
        model = Especialidade
        fields = ['nomeEspecialidade', 'cbos']

class ProcedimentoForm(forms.ModelForm):
    class Meta:
        model = Procedimento
        fields = ['descricaoProcedimento', 'tipoProcedimento']

class LocalAtendimentoForm(forms.ModelForm):
    class Meta:
        model = LocalAtendimento
        fields = ['enderecoAtendimento', 'nomeMedico', 'especialidade']


class AtendimentoForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = ['nomeBeneficiario', 'nomeMedico', 'nomeEspecialidade', 'enderecoAtendimento', 'tipoProcedimento', 'dataAtend']






