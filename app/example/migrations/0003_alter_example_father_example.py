# Generated by Django 3.2.7 on 2021-09-03 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0002_example_father_example'),
    ]

    operations = [
        migrations.AlterField(
            model_name='example',
            name='father_example',
            field=models.ForeignKey(blank=True, help_text="Luke i'm your father!", null=True, on_delete=django.db.models.deletion.CASCADE, to='example.example', verbose_name='Father'),
        ),
    ]
