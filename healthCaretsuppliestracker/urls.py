from django.conf.urls import url
from . views import RegisterView, LoginView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns=[
    url('register/', RegisterView.as_view(), name='register'),
    url('login/', LoginView.as_view(), name='login'), 
    url('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # url('logout/', LogoutView.as_view(), name='logout'), 
    
]