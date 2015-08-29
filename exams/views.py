from django.shortcuts import render, get_object_or_404
from exams.models import Questions
from django.http import HttpResponse

# Create your views here.

def displayques(request,num):
    ques =get_object_or_404(Questions,qnum=num)
    
    return HttpResponse("qnum: %s <br/> qtext: %s <br/>A) %s <br/>B) %s <br/>C) %s <br/>D) %s" % (ques.qnum,ques.qtext,ques.r1,ques.r2,ques.r3,ques.r4))
    
    