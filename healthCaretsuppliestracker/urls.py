from django.conf.urls import url

from .views import DonorView, HospitalView, ItemView,StatusView


urlpatterns=[
    url('honor/', DonorView.as_view(), name='donor'),
    url('hospital/', HospitalView.as_view(), name='hospital'),
    url('item/', ItemView.as_view(), name='item'),
    url('status/', StatusView.as_view(), name='status'),
    
]
