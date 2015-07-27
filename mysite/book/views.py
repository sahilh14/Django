from django.shortcuts import render


def book(request):
    return render(request, 'booktemplate')
# Create your views here.
