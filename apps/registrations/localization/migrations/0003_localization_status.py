# Generated by Django 2.2.6 on 2019-10-28 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localization', '0002_localization_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='localization',
            name='status',
            field=models.CharField(choices=[('P', 'Pendente'), ('I', 'Em andamento'), ('C', 'Concluído')], default='P', max_length=1, verbose_name='Situação'),
        ),
    ]
