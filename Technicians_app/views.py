from django.shortcuts import render


def welcome(request):
    return render(request, 'welcome.html')


def contact(request):
    return render(request, 'contact.html')