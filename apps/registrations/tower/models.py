from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..client.models import Client
from ..company.models import Company

PEDDING = 'P'
COMPLETED = 'C'

STATUS = (
    (PEDDING, 'Pendente'),
    (COMPLETED, 'Concluído'),
)

class Tower(models.Model):
    code = models.CharField(_('Código'), max_length=10)
    description = models.CharField(_('Descrição'), max_length=300)
    latitude = models.CharField(_('Latitude'), max_length=100, null=True)
    longitude = models.CharField(_('Longitude'), max_length=100, null=True)
    status = models.CharField(_('Status'), max_length=1, choices=STATUS, default=PEDDING)
    
    client = models.OneToOneField(Client, verbose_name=_("Cliente"), null=True, related_name='towers',
                                on_delete=models.CASCADE)
    company = models.ForeignKey('company.Company', verbose_name=_('Empresa'), null=True, related_name='towers',
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Torre')
        verbose_name_plural = _('Torres')
        db_table = 'tower'
