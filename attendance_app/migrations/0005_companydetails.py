# Generated by Django 5.0.6 on 2024-05-24 16:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_app', '0004_remove_state_nation_delete_city_delete_nation_and_more'),
        ('master', '0004_departmentmaster_designationmaster'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('reg_no', models.CharField(blank=True, max_length=100, null=True)),
                ('company_icon', models.ImageField(blank=True, null=True, upload_to='')),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.citymaster')),
            ],
        ),
    ]
