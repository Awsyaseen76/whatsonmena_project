from rest_framework import serializers
from . import models

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Auth
        # fields = ('id', 'email', 'password', 'createdAt', 'updatedAt')
        fields = '__all__'