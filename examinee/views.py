from django.shortcuts import render
from django.http import HttpResponse
from examinee.models import ExamType, Examinee
from invigilator.models import Invigilator
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
    answer1 = request.POST['fname']
    answer2 = request.POST['lname']
    answer3 = request.POST['invigid']
    answer4 = request.POST['exam']
    
    ne = Examinee()
    ne.first_name = request.POST['fname']
    ne.last_name = request.POST['lname']
    ne.regnum = request.POST['regnum']
    ne.email = request.POST['email']
    ne.exam_type = ExamType.objects.get(pk=request.POST['exam'])
    ne.invigilator = Invigilator.objects.get(pk=request.POST['invigid'])
    ne.dob = request.POST['dob']
    ne.intended = request.POST['examdate']
    #ne.approved = "no"
    
    ne.save()
    
    return HttpResponse("Hello, %s %s <br/> you selected invigilator %s and exam %s" %(answer1, answer2, answer3, answer4))
    