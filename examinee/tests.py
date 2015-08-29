from django.test import TestCase
from examinee.models import Examinee
from exams.models import ExamType
from invigilator.models import Invigilator, Institution
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.shortcuts import redirect
import os, random


# create test examinee names
def createtestexaminees(request,num):
    Examinee.objects.all().delete()
    fresults = getfileinput("static/files/fnames.csv")
    lresults = getfileinput("static/files/lnames.csv")
    invigs = Invigilator.objects.all()
    examtypes = ExamType.objects.all()
   
    fnames = []
    lnames = []
    inames = []
    
   
    for x in range(0,int(num)):
        fname = random.choice(fresults)
        fnames.append(fname)
        lname = random.choice(lresults)
        lnames.append(lname)
        iname = random.choice(invigs)
        inames.append(iname)
        etype = random.choice(examtypes)
        ne = Examinee()
        ne.first_name = fname
        ne.last_name = lname
        ne.regnum = "123"
        ne.invigilator = iname
        ne.exam_type = etype
        ne.email = fname+"@"+lname+".com"
        ne.dob = getrandomdob()
        ne.intended = getrandomintended()
        ne.save()
    
    return redirect("/admin/examinee/examinee/")
    
def getfileinput(filename):
    fo = open(filename,"r")
    line = fo.readlines()
    fo.close()
    results=[]
    for eachline in line:
        foo = eachline.strip('\n')
        results.append(foo)
    return results
    
def getrandomdob():
    age = random.randint(21,65)
    bday = random.randint(0,364)
    delta = age*365+bday
    now =  datetime.now()
    date = now - timedelta(days=delta)
    return date
    

def getrandomintended():
    intenddays = random.randint(45,182)
    now = datetime.now()
    date = now + timedelta(intenddays)
    return date
