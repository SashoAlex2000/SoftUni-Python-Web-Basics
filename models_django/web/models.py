import datetime

from django.db import models


# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class Project(models.Model):
    name = models.CharField(max_length=30)
    # employee_id = models.ForeignKey(
    #     Employee,
    #     on_delete=models.RESTRICT
    # )
    deadline = models.DateField(
        default=datetime.date(2022, 12, 12)
    )

    def __str__(self):
        return f'{self.name}'


class Employee(models.Model):
    class Meta:
        ordering = ('years_of_experience',)

    LEVEL_JUNIOR = 'Junior'
    LEVEL_MID = 'Mid-level'
    LEVEL_SENIOR = 'Senior'

    LEVELS = (
        (LEVEL_JUNIOR, LEVEL_JUNIOR),
        (LEVEL_MID, LEVEL_MID),
        (LEVEL_SENIOR, LEVEL_SENIOR),
    )

    first_name = models.CharField(
        max_length=30
    )
    review = models.TextField()

    years_of_experience = models.PositiveIntegerField()
    age = models.PositiveIntegerField()

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    level = models.CharField(
        max_length=10,
        choices=LEVELS,
        verbose_name='Seniority level',
        default=LEVEL_JUNIOR
    )

    project = models.ManyToManyField(Project)

    def __str__(self):
        return f'{self.first_name}'


class AccessCard(models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True
    )
