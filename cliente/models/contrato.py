from django.db import models
from cliente.models import Pessoa
import base64


class DocumentoContrato(models.Model):
    date_create = models.DateTimeField(auto_now_add=True)

    cliente = models.ForeignKey(Pessoa, models.DO_NOTHING, related_name='cliente_documentos')
    documento = models.FileField(verbose_name='Documento', max_length=2000, upload_to='documento_contrato')
    # doc_base64 = models.BinaryField(blank=True, null=True)
    doc_base64_txt = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["cliente"]

    def doc_base64_encode(self):
        img_base64 = base64.b64encode(self.doc_base64).decode('utf-8')
        return img_base64

