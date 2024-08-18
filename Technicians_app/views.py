from django.shortcuts import render


def welcome(request):
    return render(request, 'welcome.html')

def about_us(request):
    return render(request, 'about_us.html')

