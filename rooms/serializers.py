from rest_framework import serializers
from .models import Room
from shows.models import Show



# class upcomingShowSerializer(serializers.ModelSerializer):
#   movie = serializers.SerializerMethodField()
#   class Meta:
#     model = Show
#     fields = ('movie' , 'startTime')
  


class RoomSerializer(serializers.ModelSerializer):
  # shows = upcomingShowSerializer( many=True, read_only=True , default = [])
  class Meta:
    model = Room
    fields = "__all__"
    # fields = ('name' , 'seating_capacity','shows') 

  def validate_name(self,value):
    qs = Room.objects.filter(name = value)
    if(self.instance):
      qs = qs.exclude(pk = self.instance.pk)
    if(qs.exists()):
      raise serializers.ValidationError("{}  has already been used".format(value))
    return value


