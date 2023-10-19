from django.db import models
from cliente.models import Pessoa


class DocumentoContrato(models.Model):
    date_create = models.DateTimeField(auto_now_add=True)

    cliente = models.ForeignKey(Pessoa, models.DO_NOTHING, related_name='cliente_documentos')
    documento = models.FileField(verbose_name='Documento', max_length=2000, upload_to='documento_contrato')

    class Meta:
        ordering = ["cliente"]
