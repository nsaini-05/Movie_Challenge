from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
  class Meta:
    model = Room
    fields = '__all__'

  def validate_name(self,value):
    qs = Room.objects.filter(name = value)
    if(self.instance):
      qs = qs.exclude(pk = self.instance.pk)
    if(qs.exists()):
      raise serializers.ValidationError("{}  has already been used".format(value))
    return value