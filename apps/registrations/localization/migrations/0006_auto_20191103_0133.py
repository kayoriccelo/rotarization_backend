# Generated by Django 2.2.6 on 2019-11-03 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localization', '0005_auto_20191101_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localization',
            name='status',
            field=models.CharField(choices=[('P', 'Pendente'), ('C', 'Concluído')], default='P', max_length=1, verbose_name='Situação'),
        ),
    ]
