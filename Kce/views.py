from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return HttpResponse("<h1>My first Project</h1>")
