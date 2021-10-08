from django.conf.urls import url

urlpatterns=[
    url('item/', ItemView.as_view(), name='item'),
]
