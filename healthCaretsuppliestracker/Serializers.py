from rest_framework import serializers
from .models import *

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = ['id', 'name', 'email', 'phone_number', 'location']

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['id', 'name', 'email', 'phone_number', 'location']

class StatuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Status
        fields=['status']

    def validate(self, attrs):
        status=attrs.get('status', '')

        if not status.isalpha:
            raise serializers.ValidationError('Only alphabets are required')

        return attrs

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields=['id','item_name', 'quantity', 'description', 'order_status']