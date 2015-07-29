from django.shortcuts import render
from .models import Book

def book(request):
    return render(request, 'booktemplate')

def search_form(request):
    return render(request, 'search-form.html')
    
def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html',
                {'books': books, 'query': q})
    return render(request, 'search-form.html',
        {'error': error})