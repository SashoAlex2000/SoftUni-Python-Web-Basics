from django.db import models


# Create your models here.


class Profile(models.Model):
    FNAME_MAX_LENGTH = 20
    LNAME_MAX_LENGTH = 20

    first_name = models.CharField(
        max_length=FNAME_MAX_LENGTH,
        blank=False,
        null=False,
    )

    last_name = models.CharField(
        max_length=LNAME_MAX_LENGTH,
        blank=False,
        null=False,
    )

    age = models.IntegerField(
        blank=False,
        null=False,
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.age}'


class Note(models.Model):
    NOTE_TITLE_MAX_LEN = 30

    note_title = models.CharField(
        max_length=NOTE_TITLE_MAX_LEN,
        blank=False,
        null=False,
    )

    note_image_url = models.URLField(
        blank=False,
        null=False,
    )

    note_content = models.TextField(
        blank=False,
        null=False,
    )

    class Meta:
        ordering = (
            'pk',
        )

