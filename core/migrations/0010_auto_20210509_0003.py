# Generated by Django 2.2.21 on 2021-05-09 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210508_2347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='local',
            options={'verbose_name': 'Local', 'verbose_name_plural': 'Locais'},
        ),
        migrations.AddField(
            model_name='imovel',
            name='local',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Local'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='local',
            name='nome',
            field=models.CharField(max_length=10),
        ),
    ]
