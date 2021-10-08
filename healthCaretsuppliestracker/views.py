from django.shortcuts import render
from .Serializers import DonorSerializer,HospitalSerializer,ItemSerializer,StatuSerializer
from rest_framework import generics,status
from rest_framework.response import Response




# Create your views here.
class DonorView(generics.GenericAPIView):
    serializer_class=DonorSerializer

    def post(self, request):
        status=request.data
        serializer=self.serializer_class(data=status)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data=serializer.data
        
        return Response(user_data )

class HospitalView(generics.GenericAPIView):
    serializer_class=HospitalSerializer

    def post(self, request):
        status=request.data
        serializer=self.serializer_class(data=status)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data=serializer.data
        
        return Response(user_data )

class ItemView(generics.GenericAPIView):
    serializer_class=ItemSerializer

    def post(self, request):
        status=request.data
        serializer=self.serializer_class(data=status)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data=serializer.data
        
        return Response(user_data )

class StatusView(generics.GenericAPIView):
    serializer_class=StatuSerializer

    def post(self, request):
        status=request.data
        serializer=self.serializer_class(data=status)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data=serializer.data
        
        return Response(user_data )