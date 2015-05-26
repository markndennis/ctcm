from django.test import TestCase
from exams.models import ExamType
from django.shortcuts import redirect

# Create your tests here.
examtypes=["Acupuncturist","Herbalist","Reciprocity","Doctor of TCM"]

def createexamtype(request):
    ExamType.objects.all().delete()
    
    for mytype in examtypes:
        nt = ExamType()
        nt.exam_type = mytype
        nt.save()
        
    return redirect("/admin/exams/examtype/")
    
        