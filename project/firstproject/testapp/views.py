from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Hello_World_view(request):
    return HttpResponse('<h1>this is responce from django application </h1>')
