from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def greeting_view(Request):
    return HttpResponse('<h1> hello friends good morning have a nice day bro </h1>')
