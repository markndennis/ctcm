from django.shortcuts import render
from django.http import HttpResponse
from examinee.models import ExamType
from invigilator.models import Invigilator
import datetime

# Create your views here.

def home(request):
    context = {'title' : 'Examinee Home'}
    return render(request, 'examinee/home.html', context)
    
def apply(request):
    exam_types = ExamType.objects.all()
    invig_list = Invigilator.objects.order_by('institution','last_name')
    intend_date = str(datetime.datetime.now()+datetime.timedelta(30))
    context = {
        'title' : 'Exam Application',
        'exam_types' : exam_types,
        'invig_list' : invig_list,
        'intend_date' : intend_date,
        }
    return render(request, 'examinee/apply.html', context)