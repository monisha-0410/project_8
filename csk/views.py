from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def msd(request):
    return HttpResponse("cool king")

def raina(request):
    return HttpResponse("mr IPL")