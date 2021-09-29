from rest_framework import serializers
from .models import Movie



class MovieSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = '__all__'

  def validate_title(self,value):
    qs = Movie.objects.filter(title__iexact = value)
    if(self.instance):
      qs = qs.exclude(pk = self.instance.pk)
    if(qs.exists()):
      raise serializers.ValidationError("{} title has already been used".format(value))
    return value