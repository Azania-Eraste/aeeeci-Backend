from rest_framework import serializers
from .models import CustomUser, ScoutUser

class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class ScoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoutUser
        fields = '__all__'