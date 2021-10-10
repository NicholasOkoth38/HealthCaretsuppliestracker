from django.shortcuts import render
from rest_framework import generics,status, views
from rest_framework_simplejwt.state import User
from . serializers import RegisterSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, Token
from .utils import Mail
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.
class RegisterView(generics.GenericAPIView):
    serializer_class=RegisterSerializer

    def post(self, request):
        user=request.data
        serializer=self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data=serializer.data
        user=User.objects.get(email=user_data['email'])

        token=RefreshToken.for_user(user).access_token
        
        email_body='Hi '+user.name+' welcome to our application.'

        data={'email_body':email_body, 'to_email':user.email, 'email_subject': 'welcome'}
        Mail.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED )

class LoginView(generics.GenericAPIView):
    serializer_class=LoginSerializer

    def post(self, request):
       
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
   

        return Response(serializer.data, status=status.HTTP_200_OK)