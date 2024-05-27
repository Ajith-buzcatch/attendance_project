# Generated by Django 5.0.6 on 2024-05-27 05:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0009_alter_employeemaster_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Slno', models.IntegerField(blank=True, max_length=50, null=True)),
                ('login_datetime', models.DateTimeField(blank=True, null=True)),
                ('logout_datetime', models.DateTimeField(blank=True, null=True)),
                ('login_ipaddress', models.CharField(blank=True, max_length=1000, null=True)),
                ('logout_ipaddress', models.CharField(blank=True, max_length=1000, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.companydetails')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.employeemaster')),
            ],
        ),
    ]