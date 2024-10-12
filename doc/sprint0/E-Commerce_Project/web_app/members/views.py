from django.shortcuts import render           # added this (w3)
from django.http import HttpResponse          # added this (w3)

# Create your views here.

def members(request):                          # added this (w3)
    return HttpResponse("Hello BargainBox Customer!")     # added this (w3)
