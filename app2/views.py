from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2_first(request):
    return HttpResponse('<h3><marquee>Be happy!!!!!!</h3></marquee>')
def app2_second(request):
    return HttpResponse('<h3>hello!!!!!</h3>')
