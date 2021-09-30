from django.shortcuts import render
from .models import Ticket
from .serializers import TicketSerializer
from rest_framework import generics

# Create your views here.


class TicketList(generics.ListCreateAPIView):
  queryset = Ticket.objects.all()  
  serializer_class = TicketSerializer  



class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Ticket.objects.all()
  serializer_class = TicketSerializer