from django.shortcuts import render, get_object_or_404
from exams.models import Questions
from django.http import HttpResponse

# Create your views here.

def displayques(request,num):
    ques =get_object_or_404(Questions,qnum=num)
    
    return HttpResponse("qnum: %s <br/> qtext: %s <br/>qtext_c: %s" % (ques.qnum,ques.qtext,ques.qtext_c))