from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator, MinLengthValidator
from django.urls import reverse

# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length = 50, validators=[MaxLengthValidator(50), MinLengthValidator(8)])
    Position = models.CharField(max_length = 50)
    Office = models.CharField(max_length = 50)
    Age = models.IntegerField(validators=[MinValueValidator(13)])

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse("crud:index") 