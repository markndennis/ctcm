from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {'title' : 'Examinee Home'}
    return render(request, 'examinee/home.html', context)
    
def apply(request):
    context = {'title' : 'Exam Application'}
    return render(request, 'examinee/apply.html', context)