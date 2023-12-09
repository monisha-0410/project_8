from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def rohit(request):
    return HttpResponse("People are stunned when watching Your Performance")

def sandeep(request):
    return HttpResponse("Sandeep Warrier is an Indian international cricketer who plays as a right-arm medium-fast bowler.")