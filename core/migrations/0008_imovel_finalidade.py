# Generated by Django 2.2.21 on 2021-05-08 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210508_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='imovel',
            name='finalidade',
            field=models.CharField(choices=[('residencial', 'Residencial'), ('comercial', 'Comercial')], default=1, max_length=6),
            preserve_default=False,
        ),
    ]
