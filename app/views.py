from django.shortcuts import render


def home(request):
    return render(request, 'app/home.html')

def services(request):
    return render(request, 'app/services.html')

def shop(request):
    return render(request, 'app/shop.html')

def blog(request):
    return render(request, 'app/blog.html')

def contact(request):
    return render(request, 'app/contact.html')

