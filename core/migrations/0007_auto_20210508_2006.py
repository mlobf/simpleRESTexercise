# Generated by Django 2.2.21 on 2021-05-08 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_imobiliaria_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='imovel',
            name='status',
            field=models.CharField(choices=[('ativo', 'Ativo'), ('inativo', 'Inativo')], default=1, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imovel',
            name='tipo',
            field=models.CharField(choices=[('casa', 'Casa'), ('apartamento', 'Apartamento')], default=1, max_length=6),
            preserve_default=False,
        ),
    ]
