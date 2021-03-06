from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse
from django.template.loader import get_template

import datetime

def index(request):
    return HttpResponse("Hello.You are at polls index.")
    
def main1(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now <br> %s</body></html>"%now
    return HttpResponse(html)

def main2(request):
    now = datetime.datetime.now()
    c = Context({'now' : now})
    t = get_template('mytemplate.html')
    html = t.render(c)
    return HttpResponse(html)

def main(request):
    now = datetime.datetime.now()
    return render(request, 'mytemplate.html', {'now':now})              ## render returns a HttpResponse object
# Create your views here.
