# Generated by Django 2.2.16 on 2020-10-19 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0003_auto_20201019_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='subject',
            field=models.CharField(max_length=200, verbose_name='Polling Subject'),
        ),
    ]
