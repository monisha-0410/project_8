from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat(request):
    return HttpResponse("fav Batsman")

def Glenn(request):
    return HttpResponse("Glenn is known as explosive batting and innovative shots, such as reverse sweeps and pulls")