from django.conf.urls import url
from . views import RegisterView, verifyEmail

urlpatterns=[
    url('register/', RegisterView.as_view(), name='register'), 
    url('email-verify/', verifyEmail.as_view(), name='verify-email'), 

     
]