from rcb.views import *
from django.urls import path
app_name="Everything"
urlpatterns=[
    path('virat/',virat,name='virat'),
    path('Glenn/',Glenn,name='Glenn')
    ]