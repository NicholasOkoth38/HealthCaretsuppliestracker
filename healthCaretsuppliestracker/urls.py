from django.conf.urls import url
from . views import RegisterView, LoginView

urlpatterns=[
    url('register/', RegisterView.as_view(), name='register'),
    url('login/', LoginView.as_view(), name='login'), 
    
]