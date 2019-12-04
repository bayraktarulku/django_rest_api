from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world!")


def home(request):
    title = 'Django Example'
    return render(request, 'home.html', {'title': title})
