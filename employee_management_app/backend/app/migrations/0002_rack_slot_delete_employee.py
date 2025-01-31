# Generated by Django 5.1.5 on 2025-01-31 07:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rows', models.IntegerField()),
                ('columns', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.IntegerField()),
                ('column', models.IntegerField()),
                ('name', models.CharField(default='Slot', max_length=255)),
                ('rack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='app.rack')),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
