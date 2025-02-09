from rest_framework import serializers
from models import Drink

class DrinkSerializer(serializers.Modelserializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']
        