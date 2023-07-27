from django.urls import path
from app3.views import *
app_name='anonymous'

urlpatterns=[
    path('one/', one, name='one'),
    path('two/', two, name='two'),
    path('three/', three, name='three'),
]