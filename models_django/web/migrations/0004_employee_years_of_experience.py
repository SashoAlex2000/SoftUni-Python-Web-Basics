# Generated by Django 4.1.2 on 2022-10-09 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_employee_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='years_of_experience',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
