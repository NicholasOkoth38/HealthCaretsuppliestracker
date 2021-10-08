from django.conf.urls import url
from . views import RegisterView

urlpatterns=[
    url('register/', RegisterView.as_view(), name='register'),  
]