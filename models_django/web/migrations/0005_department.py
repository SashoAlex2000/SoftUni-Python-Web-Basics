# Generated by Django 4.1.2 on 2022-10-09 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_employee_years_of_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
