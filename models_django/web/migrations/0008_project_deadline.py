# Generated by Django 4.1.2 on 2022-10-09 14:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_project_employee_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='deadline',
            field=models.DateField(default=datetime.date(2022, 12, 12)),
        ),
    ]
