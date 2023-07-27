from django.urls import path
from app2.views import *
app_name='idk'

urlpatterns=[
    path('one/', one, name='one'),
    path('two/', two, name='two'),
    path('three/', three, name='three'),
]