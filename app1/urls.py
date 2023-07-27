from django.urls import path
from app1.views import *
app_name='whatever'

urlpatterns=[
    path('one/', one, name='one'),
    path('two/', two, name='two'),
    path('three/', three, name='three'),
]