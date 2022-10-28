from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.

def validate_rating(value):
    MIN_RATING = 0.1
    MAX_RATING = 5

    if value < MIN_RATING or MAX_RATING < value:
        raise ValidationError(f'The rating should be between {MIN_RATING} and {MAX_RATING}!')


class Profile(models.Model):
    MIN_AGE = 12
    PASSWORD_MAX_LENGTH = 30
    FNAME_MAX_LENGTH = 30
    LNAME_MAX_LENGTH = 30

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.IntegerField(
        validators=(
            validators.MinValueValidator(MIN_AGE),
        ),
        blank=False,
        null=False,
    )

    pasword = models.CharField(
        max_length=PASSWORD_MAX_LENGTH,
        blank=False,
        null=False,
    )

    first_name = models.CharField(
        max_length=FNAME_MAX_LENGTH,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=LNAME_MAX_LENGTH,
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )


class Game(models.Model):
    GAME_TITLE_MAX_LEN = 30
    CATEGORY_MAX_LEN = 15

    ACTION = 'Action'
    ADVENTURE = 'Adventure'
    PUZZLE = 'Puzzle'
    STRATEGY = 'Strategy'
    SPORTS = 'Sports'
    BOARD_CARD_GAME = 'Board/Card Game'
    OTHER = 'Other'

    CATEGORY_CHOICES = (
        (ACTION, ACTION),
        (ADVENTURE, ADVENTURE),
        (PUZZLE, PUZZLE),
        (STRATEGY, STRATEGY),
        (SPORTS, SPORTS),
        (BOARD_CARD_GAME, BOARD_CARD_GAME),
        (OTHER, OTHER),
    )

    game_title = models.CharField(
        max_length=GAME_TITLE_MAX_LEN,
        blank=False,
        null=False,
    )

    category = models.CharField(
        choices=CATEGORY_CHOICES,
        max_length=CATEGORY_MAX_LEN,
        blank=False,
        null=False,
    )

    rating = models.FloatField(
        validators=(
          validate_rating,
        ),
        blank=False,
        null=False,
    )

    max_level = models.IntegerField(
        validators=(
            validators.MinValueValidator(1),
        ),
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    summary = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('pk',)