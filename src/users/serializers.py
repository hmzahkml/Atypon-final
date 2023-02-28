from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'name', 'password')
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            name=validated_data.get('name', ''),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user