# Generated by Django 2.2.6 on 2019-11-01 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scripting', '0005_auto_20191029_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scripting',
            name='localizations',
            field=models.ManyToManyField(blank=True, related_name='scripting', to='localization.Localization', verbose_name='localization'),
        ),
    ]
