from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    text = "hello,world. you're at the polls index."
    return HttpResponse(text)
