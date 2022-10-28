from django.db import models


# Create your models here.

class Profile(models.Model):

    FNAME_MAX_LENGTH = 30
    LNAME_MAX_LENGTH = 30

    first_name = models.CharField(
        blank=False,
        null=False,
        max_length= FNAME_MAX_LENGTH,
    )

    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=LNAME_MAX_LENGTH,
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )


class Book(models.Model):
    BOOK_TITLE_MAX_LENGTH = 30
    BOOK_TYPE_MAX_LENGTH = 30

    book_title = models.CharField(
        max_length=BOOK_TITLE_MAX_LENGTH,
        blank=False,
        null= False,

    )

    book_description = models.TextField(
        blank=False,
        null=False,
    )

    book_image_url = models.URLField(
        blank=False,
        null=False,
    )

    book_type = models.CharField(
        max_length=BOOK_TYPE_MAX_LENGTH,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ('pk',)

