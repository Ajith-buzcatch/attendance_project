# Generated by Django 5.0.6 on 2024-05-27 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0013_rename_employee_id_employeemaster_employee_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendancemaster',
            options={'verbose_name': 'AttendanceMaster'},
        ),
        migrations.AlterModelOptions(
            name='citymaster',
            options={'verbose_name': 'CityMaster'},
        ),
        migrations.AlterModelOptions(
            name='companydetails',
            options={'verbose_name': 'CompanyDetails'},
        ),
        migrations.AlterModelOptions(
            name='departmentmaster',
            options={'verbose_name': 'DepartmentMaster'},
        ),
        migrations.AlterModelOptions(
            name='designationmaster',
            options={'verbose_name': 'DesignationMaster'},
        ),
        migrations.AlterModelOptions(
            name='employeedepartment',
            options={'verbose_name': 'EmployeeDepartment'},
        ),
        migrations.AlterModelOptions(
            name='employeedesignation',
            options={'verbose_name': 'EmployeeDesignation'},
        ),
        migrations.AlterModelOptions(
            name='employeeimage',
            options={'verbose_name': 'EmployeeImage'},
        ),
        migrations.AlterModelOptions(
            name='employeejoinmaster',
            options={'verbose_name': 'EmployeeJoinMaster'},
        ),
        migrations.AlterModelOptions(
            name='employeemaster',
            options={'verbose_name': 'EmployeeMaster'},
        ),
        migrations.AlterModelOptions(
            name='nationmaster',
            options={'verbose_name': 'NationMaster'},
        ),
        migrations.AlterModelOptions(
            name='statemaster',
            options={'verbose_name': 'StateMaster'},
        ),
    ]