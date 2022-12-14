# Generated by Django 4.1.2 on 2022-10-30 07:58

import django.core.validators
from django.db import migrations, models
import final_exam.web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_type', models.CharField(choices=[('Sports Car', 'Sports Car'), ('Pickup', 'Pickup'), ('Crossover', 'Crossover'), ('Minibus', 'Minibus'), ('Other', 'Other')], max_length=10)),
                ('car_model', models.CharField(max_length=20, validators=[final_exam.web.models.validate_min_model_name_length])),
                ('car_year', models.IntegerField(validators=[final_exam.web.models.validate_car_year])),
                ('car_image_url', models.URLField()),
                ('car_price', models.FloatField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
    ]
