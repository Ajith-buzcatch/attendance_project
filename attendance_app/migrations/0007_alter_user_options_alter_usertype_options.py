# Generated by Django 5.0.6 on 2024-05-27 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_app', '0006_delete_companydetails'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'UserMaster'},
        ),
        migrations.AlterModelOptions(
            name='usertype',
            options={'verbose_name': 'UserType'},
        ),
    ]
