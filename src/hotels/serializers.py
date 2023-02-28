from rest_framework import serializers

import .models Hotel

class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = ('name', 'address','description')