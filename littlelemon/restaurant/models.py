from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField()
    bookingdate = models.DateTimeField()

    def __str__(self): 
        return self.name

# class Menu(models.Model):
#    title = models.CharField(max_length=200) 
#    price = models.FloatField() 
#    inventory = models.IntegerField()

#    def __str__(self):
#        return f'{self.title} : {str(self.price)}'
   


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    
    def get_item(self):
        return f'{self.title} : {str(self.price)}'
