from django.shortcuts import render

from healthCaretsuppliestracker.models import Donor
from .Serializers import DonorSerializer,HospitalSerializer,ItemSerializer,StatuSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from .permission import IsAdminOrReadOnly
from django.http import Http404


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

####

class donorDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    # def get_donor(self, pk):
    #     try:
    #         return Donor.objects.get(pk=pk)
    #     except Donor.DoesNotExist:
    #         return Http404

    def get(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = DonorSerializer(merch)
        return Response(serializers.data)

####


# def delete(self, request, pk, format=None):
#     merch = self.get_merch(pk)
#     merch.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)

####
