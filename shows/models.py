from django.db import models
from movies.models import Movie
from rooms.models import Room
from django.core.validators import MinValueValidator

# Create your models here.
class Show(models.Model):
  room  = models.ForeignKey(Room , on_delete = models.CASCADE)
  movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
  startTime = models.DateTimeField(blank = False)
  price = models.DecimalField(max_digits = 4 ,decimal_places = 2)


  def __str__(self):
    return self.room.name + "" + self.movie.title + "" + self.startTime 

  