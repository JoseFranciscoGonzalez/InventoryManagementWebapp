# Generated by Django 3.2.9 on 2022-02-08 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='isbn',
        ),
        migrations.AddField(
            model_name='material',
            name='safety_stock',
            field=models.IntegerField(blank=True, help_text='Mínimo stock recomendado', null=True, verbose_name='Stock de seguridad'),
        ),
    ]
