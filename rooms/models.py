from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Room(models.Model):
  name = models.CharField(max_length=10)
  seating_capacity = models.PositiveIntegerField(default = 0 , validators=[MinValueValidator(0)] )
  
  
  def __str__(self):
    return self.name
