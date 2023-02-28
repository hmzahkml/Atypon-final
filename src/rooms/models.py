from django.db import models

from hotels.models import Hotel

# Create your models here.

class Room(models.Model):
    ROOM_TYPES = (
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite')
    )

    number = models.IntegerField()
    type = models.CharField(max_length=10, choices=ROOM_TYPES)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)