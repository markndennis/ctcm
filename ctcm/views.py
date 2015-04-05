from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome(request):
    context = {'title' : 'Welcome'}
    return render(request, 'welcome.html', context)
    
    
def about(request):
    context = {'title' : 'About'}
    return render(request, 'about.html', context)
        