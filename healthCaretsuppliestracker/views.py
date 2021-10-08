from django.shortcuts import render
from rest_framework import generics,status
from rest_framework_simplejwt.state import User
from . serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import Mail
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

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
        current_site=get_current_site(request).domain
        relativeLink=reverse('verify-email')
        
        absurl='http://'+current_site+relativeLink+"?token="+str(token)
        email_body='Hi'+user.name+'use the link below to verify your email.\n'+absurl

        data={'email_body':email_body, 'to_email':user.email, 'email_subject': 'verify your email'}
        Mail.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED )

class verifyEmail(generics.GenericAPIView):
    def get(self):
        pass
    