from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.

def welcome(request):
    context = {'title' : 'Welcome'}
    return render(request, 'welcome.html', context)
    
    
def about(request):
    context = {'title' : 'About'}
    return render(request, 'about.html', context)
    
    
def mail(to,cc,subject,message):
    mailfrom = "markndennis@hotmail.com"
    send_mail(subject, message, mailfrom, [to], fail_silently=False)
    return