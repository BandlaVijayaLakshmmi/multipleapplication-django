from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_first(request):
    return HttpResponse('<h1><p>srujana and</p> siri college friends</h1>')
def app1_second(request):
    return HttpResponse('<h1><marquee>srujana and siri tom and jerry</h1></marquee>')