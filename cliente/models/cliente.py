from django.db import models


class Pessoa(models.Model):
    date_create = models.DateTimeField(auto_now_add=True)

    nome = models.CharField(max_length=255, verbose_name='NOME COMPLETO')
    cpf = models.CharField(max_length=255, verbose_name='CPF', help_text='000.000.000-00')
    fone = models.CharField(max_length=15, verbose_name='TELEFONE', help_text='Dê preferência ao número do Whatsapp')

    doc_inserido = models.BooleanField(default=False)
    contrato_enviado = models.BooleanField(default=False, verbose_name='CONTRATO ENVIADO')

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome.upper()

    def document_mask(self):
        if len(self.cpf) == 11:
            mask = '{}.{}.{}-{}'.format(self.cpf[:3], self.cpf[3:6], self.cpf[6:9], self.cpf[9:])
        elif len(self.cpf) == 14:
            mask = '{}.{}.{}/{}-{}'.format(self.cpf[:2], self.cpf[2:5], self.cpf[5:8], self.cpf[8:12], self.cpf[12:])
        else:
            return None
        return mask

    def fone_mask(self):
        mask = '({}) {} {}-{}'.format(self.fone[:2], self.fone[2:3], self.fone[3:7], self.fone[7:11])
        return mask
