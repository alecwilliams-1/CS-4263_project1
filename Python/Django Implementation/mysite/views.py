
from django.shortcuts import render
from random import *

def home(request):
    return render(request, 'home.html', {"number": randint(1,1000000)} )
