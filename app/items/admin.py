from django.contrib import admin
from .models import Beneficiario
from .models import Medico
from .models import Especialidade
from .models import LocalAtendimento
from .models import Procedimento
from .models import Atendimento

# Register your models here.

admin.site.register(Beneficiario)
admin.site.register(Medico)
admin.site.register(Especialidade)
admin.site.register(LocalAtendimento)
admin.site.register(Procedimento)
admin.site.register(Atendimento)
