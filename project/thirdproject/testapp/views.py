from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def good_morning_view(request):
    return HttpResponse('<h1>Hello freind good morning </h1>')

def good_night_view(request):
    return HttpResponse('<h1>Hello freind good night </h1>')

def good_afternoon_view(request):
    return HttpResponse('<h1>Hello freind good afternoon </h1>')
