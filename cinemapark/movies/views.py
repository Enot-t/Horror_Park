from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def TheSilenceoftheLambs(request):
    return render(request, 'movie3.html')

def  TheShining(request):
    return render(request, 'movie2.html')

def Sinister(request):
    return render(request, 'movie.html')