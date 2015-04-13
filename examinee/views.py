from django.shortcuts import render
from django.http import HttpResponse
from examinee.models import ExamType, Examinee
from invigilator.models import Invigilator
from django.core.mail import send_mail
from ctcm.views import mail
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required

import datetime

# Create your views here.

def home(request):
    context = {'title' : 'Examinee Home'}
    return render(request, 'examinee/home.html', context)
    
def apply(request):
    exam_types = ExamType.objects.all()
    invig_list = Invigilator.objects.order_by('institution','last_name')
    intend_date = (datetime.datetime.now()+datetime.timedelta(30))
    intend_date = intend_date.strftime('%Y-%m-%d')
    context = {
        'title' : 'Exam Application',
        'exam_types' : exam_types,
        'invig_list' : invig_list,
        'intend_date' : intend_date,
        }
    return render(request, 'examinee/apply.html', context)
    
def application(request):
    postdata={
    'fname' : request.POST['fname'],
    'lname' : request.POST['lname'],
    'regnum' : request.POST['regnum'],
    'email' : request.POST['email'],
    'exam' : ExamType.objects.get(pk=request.POST['exam']),
    'invigilator' : Invigilator.objects.get(pk=request.POST['invigid']),
    'intended' : request.POST['examdate'],
    'dob' : request.POST['dob'],
    }
    
    ne = Examinee()
    ne.first_name = postdata['fname']
    ne.last_name = postdata['lname']
    ne.regnum = postdata['regnum']
    ne.email = postdata['email']
    ne.exam_type = postdata['exam']
    ne.invigilator = postdata['invigilator']
    ne.dob = postdata['dob']
    ne.intended = postdata['intended']
    ne.save()
    
    #mail("markndennis@hotmail.com","markndennis@hotmail.com","test mail","%s this is your test mail" %answer1)
    #return HttpResponse("Hello, %s %s <br/> you selected invigilator %s and exam %s" %(answer1, answer2, answer3, answer4))
    
    return render(request, 'examinee/applicationConfirmation.html', postdata)
    

@login_required
def examineelist(request):
    object_list = Examinee.objects.order_by('last_name')
    user_greeting = "Welcome "+request.user.first_name + "!"
    context = {'object_list':object_list,'title':'Examinee List', 'user_greeting':user_greeting}
    return render(request, 'examinee/examinee_list.html', context)
    


# class ExamineeListView(ListView):
#     model = Examinee
    
#     @login_required
#     def get_context_data(self, **kwargs):
#         context = super(ExamineeListView, self).get_context_data(**kwargs)
#         context['title'] = "Examinee List Generic View"
#         return context