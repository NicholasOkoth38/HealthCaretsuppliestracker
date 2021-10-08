from django.db.models import fields
from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=50, min_length=8, write_only=True)

    class Meta:
        model=User
        fields=['id','name', 'email', 'phone_number', 'location', 'password']

    