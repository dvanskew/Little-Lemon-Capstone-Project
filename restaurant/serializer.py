from rest_framework import serializers
from .models import menu, booking

# Serializers define the API representation.

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = "__self__"
        
    def create(self, validated_data):
        return menu.objects.create(**validated_data)
        
class BookingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = booking
        fields = "__self__"   
        
    def create(self, validated_data):
        return booking.objects.create(**validated_data)
        