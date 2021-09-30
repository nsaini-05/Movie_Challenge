from rest_framework import serializers
from django.db.models import Sum

from .models import Ticket
from shows.models import Show



class TicketSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ticket
    fields = ['id','customer_name','show','seats','amount']
    read_only_fields = ['amount']
  

  def validate(self, data):
   qs = Ticket.objects.filter(show = data['show'])
   available_seats =  data['show'].room.seating_capacity - sum([item.seats for item in qs]) 
   if(data['seats'] > available_seats):
     raise serializers.ValidationError("No More seats for this show. Seats available: {}".format(available_seats))   

 
  #  print(data['show'].available_seats)
   return data
