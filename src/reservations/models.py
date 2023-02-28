from django.db import models
from rooms.models import Room
from users.models import CustomUser
# Create your models here.
class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    is_paid = models.BooleanField(default=False)