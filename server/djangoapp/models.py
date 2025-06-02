# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


# Create your models here.

from django.db import models


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake,
                                 on_delete=models.CASCADE)  # Many-to-One
    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Weitere auf Wunsch
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        default=datetime.datetime.now().year,
        validators=[
            MaxValueValidator(datetime.datetime.now().year),
            MinValueValidator(1990)
        ]
    )
    dealer_id = models.IntegerField()  # Verknüpfung zur Cloudant-Dealer-ID

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
