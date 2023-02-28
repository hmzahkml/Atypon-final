from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)



# class Room(models.Model):
#     hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
#     room_number = models.CharField(max_length=10)
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=6, decimal_places=2)

#     def __str__(self):
#         return f'{self.hotel} - Room {self.room_number}'


# class Reservation(models.Model):
#     room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations')
#     guest_name = models.CharField(max_length=100)
#     guest_email = models.EmailField()
#     check_in = models.DateField()
#     check_out = models.DateField()
#     num_guests = models.PositiveSmallIntegerField()

#     def __str__(self):
#         return f'{self.guest_name} - {self.room}'