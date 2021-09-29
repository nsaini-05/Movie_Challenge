from django.shortcuts import render
from .models import Show
from .serializers import ShowSerializer


from rest_framework import generics
# Create your views here.
class ShowList(generics.ListCreateAPIView):
  queryset = Show.objects.all()  
  serializer_class = ShowSerializer  



class ShowDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Show.objects.all()
  serializer_class = ShowSerializer