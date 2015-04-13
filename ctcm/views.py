from django.shortcuts import render
from django.http import HttpResponse
#from django.template.response import TemplateResponse
from django.core.mail import send_mail
from django.contrib.auth import views
from django.template.response import TemplateResponse


# Create your views here.

def welcome(request):
    context = {'title' : 'Welcome'}
    return render(request, 'welcome.html', context)
    
def about(request):
    context = {'title' : 'About'}
    return render(request, 'about.html', context)
    
# def mylogin(request):
#     template_response = views.login(request)
#     template_response.context={'myvar':'myvar content'}
#     return template_response
#     #return render(request, 'registration/login.html',context)
    
def mail(to,cc,subject,message):
    mailfrom = "markndennis@hotmail.com"
    send_mail(subject, message, mailfrom, [to], fail_silently=False)
    return