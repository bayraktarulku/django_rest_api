from django.http import HttpResponse
from django.shortcuts import render
# from rest_framework import viewsets
# from helloworld.serializers import UserSerializer


def index(request):
    return HttpResponse("Hello, world!")


def home(request):
    title = 'Django Example'
    return render(request, 'home.html', {'title': title})


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = []
#     serializer_class = UserSerializer
