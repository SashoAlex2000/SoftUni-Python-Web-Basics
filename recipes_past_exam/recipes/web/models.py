from django.db import models


# Create your models here.


class Recipe(models.Model):
    TITLE_MAX_LENGTH = 30
    INGREDIENTS_MAX_LENGTH = 250

    recipe_title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        blank=False,
        null=False,
    )

    recipe_image_url = models.URLField(
        blank=False,
        null=False,
    )

    description = models.TextField(
        blank=False,
        null=False,
    )

    ingredients = models.CharField(
        blank=False,
        null=False,
        max_length=INGREDIENTS_MAX_LENGTH
    )

    time = models.IntegerField(
        blank=False,
        null=False,
    )

    def __str__(self):
        return f"{self.recipe_title}"

    class Meta:
        ordering = (
            'pk',
                    )
