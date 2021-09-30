from django.db import models
from shows.models import Show
from django.core.validators import MinValueValidator

from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.
class Ticket(models.Model):
  customer_name = models.CharField(max_length=20 , blank = False)
  show = models.ForeignKey(Show,on_delete=models.CASCADE)
  seats = models.PositiveIntegerField(default = 1 , validators=[MinValueValidator(0)])
  amount = models.DecimalField(editable=False, null =  False, max_digits = 100 ,decimal_places = 2)




@receiver(pre_save , sender = Ticket)
def getamount(instance , **kwargs):
  instance.amount =  instance.seats * instance.show.price
