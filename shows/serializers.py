from rest_framework import serializers
from .models import Show
import datetime 


def time_in_range(existingStart, existingEnd, showStart,showEnd ):
  if((existingStart <= showEnd) and (showStart <= existingEnd)):
    return True;


class ShowSerializer(serializers.ModelSerializer):
  class Meta:
    model = Show
    fields = ['id','room','movie','startTime','endTime','price']
    read_only_fields = ['endTime']


  def validate(self,data):
    startTime = data['startTime']
    endTime = data['startTime']+ datetime.timedelta(minutes = data['movie'].duration_in_mintues)
    shows = Show.objects.filter(room = data['room'])    
    for show in shows:
      if(time_in_range(show.startTime , show.endTime , startTime, endTime)):
          raise serializers.ValidationError("{}  has already been used".format(startTime))   
    
    return data 

  
 
    






  # @property
  # def endTime(self):
  #   return self.startTime + datetime.timedelta(minutes = self.movie.duration)

