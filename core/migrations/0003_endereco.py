# Generated by Django 2.2.21 on 2021-05-07 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210507_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('rua', models.CharField(max_length=255)),
                ('complemento', models.CharField(max_length=255)),
                ('cep', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': ['cidade'],
            },
        ),
    ]
