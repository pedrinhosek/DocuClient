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





class historico_canie(models.Model):
    c1 = models.TextField(blank=True, null=True)
    c2 = models.TextField(blank=True, null=True)
    c3 = models.TextField(blank=True, null=True)
    c4 = models.TextField(blank=True, null=True)
    c5 = models.TextField(blank=True, null=True)
    c6 = models.TextField(blank=True, null=True)
    c7 = models.TextField(blank=True, null=True)
    c8 = models.TextField(blank=True, null=True)
    c9 = models.TextField(blank=True, null=True)
    c10 = models.TextField(blank=True, null=True)
    c11 = models.TextField(blank=True, null=True)
    c12 = models.TextField(blank=True, null=True)
    c13 = models.TextField(blank=True, null=True)
    c14 = models.TextField(blank=True, null=True)
    c15 = models.TextField(blank=True, null=True)
    c16 = models.TextField(blank=True, null=True)
    c17 = models.TextField(blank=True, null=True)
    c18 = models.TextField(blank=True, null=True)
    c19 = models.TextField(blank=True, null=True)
    canie_json = models.TextField(blank=True, null=True)


class canie_estrutura_hidrografica(models.Model):
    c1 = models.TextField(blank=True, null=True)
    c2 = models.TextField(blank=True, null=True)
    c3 = models.TextField(blank=True, null=True)
    c4 = models.TextField(blank=True, null=True)
    c5 = models.TextField(blank=True, null=True)
    c6 = models.TextField(blank=True, null=True)
    c7 = models.TextField(blank=True, null=True)
    c8 = models.TextField(blank=True, null=True)
    c9 = models.TextField(blank=True, null=True)
