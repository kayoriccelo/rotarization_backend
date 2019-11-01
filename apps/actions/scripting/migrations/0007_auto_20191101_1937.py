# Generated by Django 2.2.6 on 2019-11-01 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scripting', '0006_auto_20191101_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scripting',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='scriptings', to='company.Company', verbose_name='Empresa'),
            preserve_default=False,
        ),
    ]
