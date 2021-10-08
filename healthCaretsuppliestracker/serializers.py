from django.db.models import fields
from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=50, min_length=8, write_only=True)

    class Meta:
        model=User
        fields=['id','name', 'email', 'phone_number', 'location', 'password']
    
    def validate(self, attrs):
        email=attrs.get('email', '')
        username=attrs.get('username', '')

        if not username.isalnum:
            raise serializers.ValidationError('The username should only contain alphanumeric characters')

        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)