# Generated by Django 5.0.6 on 2024-06-07 10:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('tel', models.CharField(max_length=12)),
                ('bloque', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('creator', models.CharField(max_length=100)),
                ('type_media', models.CharField(choices=[('livre', 'Livre'), ('cd', 'CD'), ('dvd', 'DVD'), ('Jeu_de_plateau', 'Jeu de plateau')], max_length=20)),
                ('disponible', models.BooleanField(default=True)),
                ('dateEmprunt', models.DateTimeField(blank=True, null=True)),
                ('emprunteur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bibliothecaire.membre')),
            ],
        ),
    ]