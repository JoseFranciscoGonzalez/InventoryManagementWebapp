# Generated by Django 3.2.9 on 2022-02-08 14:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('isbn', models.CharField(help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, verbose_name='ISBN')),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ingrese el nombre del sistema o equipo asociado (p. ej. Iluminación, Sistema de Vapor, etc.)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Trademark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ingrese el nombre de la marca (p. ej. Grundfos, Spirax Sarco, etc.)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID único para este material particular en toda la biblioteca', primary_key=True, serialize=False)),
                ('entry', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='m', help_text='Disponibilidad del libro', max_length=1)),
                ('material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.material')),
            ],
            options={
                'ordering': ['entry'],
            },
        ),
        migrations.AddField(
            model_name='material',
            name='system',
            field=models.ManyToManyField(help_text='Seleccione un sistema/equipo para este material', to='catalog.System'),
        ),
        migrations.AddField(
            model_name='material',
            name='trademark',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.trademark'),
        ),
    ]