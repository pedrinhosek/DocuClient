# Generated by Django 4.2.6 on 2023-10-23 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='contrato_enviado',
            field=models.BooleanField(default=False, verbose_name='CONTRATO ENVIADO'),
        ),
    ]
