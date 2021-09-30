from django.db import models
from movies.models import Movie
from rooms.models import Room
from django.core.validators import MinValueValidator
import datetime 
from django.db.models.signals import pre_save
from django.dispatch import receiver



# Create your models here.
class Show(models.Model):
  room  = models.ForeignKey(Room , on_delete = models.CASCADE)
  movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
  startTime = models.DateTimeField(blank = False)
  price = models.DecimalField(max_digits = 4 ,decimal_places = 2)
  endTime = models.DateTimeField(editable=False)

  def __str__(self):
    return self.startTime.strftime(' %d, %b %Y , %H:%M') + " Room: " + self.room.name + " Movie :" + self.movie.title 


@receiver(pre_save , sender = Show)
def getendTime(instance , **kwargs):
  instance.endTime =  instance.startTime + datetime.timedelta(minutes = instance.movie.duration_in_mintues)



