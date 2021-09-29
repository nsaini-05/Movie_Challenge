from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Movie(models.Model):
  title = models.CharField(max_length=10 , blank = False)
  duration_in_mintues = models.PositiveIntegerField(blank = False , validators=[MinValueValidator(0)] ) 
  def __str__(self):
    return self.title

 