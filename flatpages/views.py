from django.http import HttpResponse
from django.shortcuts import render
from django import template

def home(request): 

    return HttpResponse(u'hello world!', content_type="text/plain; charset=UTF-8") 
# Create your views here.
#def home_index(request): 

    #return render(request, 'templates/index.html') 
    
def home_index(request):
   
    return render(request, 'templates/static_handler.html')
