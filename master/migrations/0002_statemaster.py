# Generated by Django 5.0.6 on 2024-05-24 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(blank=True, max_length=250, null=True)),
                ('nation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.nationmaster')),
            ],
        ),
    ]
