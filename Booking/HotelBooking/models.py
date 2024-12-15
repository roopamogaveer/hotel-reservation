from django.db import models
from user.models import User


class Reservation(models.Model):
    id = models.AutoField
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotelname = models.CharField(max_length=100)
    checkin = models.DateTimeField()
    checkout =models.DateTimeField()
    nopersons = models.IntegerField()

    def __str__(self):
        return self.hotelname