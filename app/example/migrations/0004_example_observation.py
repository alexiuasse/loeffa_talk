# Generated by Django 3.2.7 on 2021-09-03 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0003_alter_example_father_example'),
    ]

    operations = [
        migrations.AddField(
            model_name='example',
            name='observation',
            field=models.TextField(blank=True, verbose_name='Observation'),
        ),
    ]
