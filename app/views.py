from django.shortcuts import render
from django.http import HttpResponse

def services(request):
    return HttpResponse('services')

def shop(request):
    return HttpResponse('shop')

def blog(request):
    return HttpResponse('blog')

def contact(request):
    return HttpResponse('contact')

