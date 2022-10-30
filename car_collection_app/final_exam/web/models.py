from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.


def validate_min_length(value):
    if len(value) < 2:
        raise ValidationError("The username must be a minimum of 2 chars")


def validate_car_year(value):
    error_string = "Year must be between 1980 and 2049"
    if value < 1980 or 2049 < value:
        raise ValidationError(error_string)


def validate_min_model_name_length(value):
    if len(value) < 2:
        raise ValidationError('Car model should be at least 2 characters')


class Profile(models.Model):
    USERNAME_MAX_LEN = 10
    PASSWORD_MAX_LEN = 30
    MIN_AGE = 18
    FNAME_MAX_LEN = 30
    LNAME_MAX_LEN = 30

    profile_username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        blank=False,
        null=False,
        validators=(
            validate_min_length,
        )
    )

    profile_email = models.EmailField(
        blank=False,
        null=False,
    )

    profile_age = models.IntegerField(
        blank=False,
        null=False,
        validators=(
            validators.MinValueValidator(MIN_AGE),
        ),
    )

    profile_password = models.CharField(
        max_length=PASSWORD_MAX_LEN,
        blank=False,
        null=False,
    )

    profile_first_name = models.CharField(
        max_length=FNAME_MAX_LEN,
        blank=True,
        null=True,
    )

    profile_last_name = models.CharField(
        max_length=LNAME_MAX_LEN,
        blank=True,
        null=True,
    )

    profile_picture_url = models.URLField(
        blank=True,
        null=True,
    )


class Car(models.Model):
    CAR_TYPE_MAX_LEN = 10
    CAR_MODEL_MAX_LEN = 20
    CAR_MODEL_MIN_LEN = 10
    CAR_PRICE_MIN = 1

    SPORTS_CAR = 'Sports Car'
    PICKUP = 'Pickup'
    CROSSOVER = 'Crossover'
    MINIBUS = 'Minibus'
    OTHER = 'Other'

    CAR_TYPES = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER),
    )

    car_type = models.CharField(
        blank=False,
        null=False,
        max_length=CAR_TYPE_MAX_LEN,
        choices=CAR_TYPES,
    )

    car_model = models.CharField(
        blank=False,
        null=False,
        max_length=CAR_MODEL_MAX_LEN,
        validators=(
            validate_min_model_name_length,
        ),
    )

    car_year = models.IntegerField(
        blank=False,
        null=False,
        validators=(
            validate_car_year,
        ),
    )

    car_image_url = models.URLField(
        blank=False,
        null=False,
    )

    car_price = models.FloatField(
        blank=False,
        null=False,
        validators=(
            validators.MinValueValidator(CAR_PRICE_MIN),
        ),
    )

    class Meta:
        ordering = (
            'pk',
        )
