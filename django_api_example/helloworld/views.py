from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world!")


def home(request):
    # return HttpResponse("Hello, world2!")
    return render(request, 'home.html', {})
