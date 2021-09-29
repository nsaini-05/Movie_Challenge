from rest_framework import serializers
from .models import Show
import datetime 



class ShowSerializer(serializers.ModelSerializer):
  endTime = serializers.SerializerMethodField()
  class Meta:
    model = Show
    fields = ['id','room','movie','startTime','endTime','price']
    read_only_fields = ['endTime']

  def get_endTime(self,obj):
    return obj.startTime + datetime.timedelta(minutes = obj.movie.duration_in_mintues)




