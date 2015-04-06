from django.db import models
#from invigilator.models import Invigilator

# Create your models here.

class ExamType(models.Model):
    exam_type= models.CharField(max_length=20)
    
    def __unicode__(self):              # __unicode__ on Python 2
        return self.exam_type


class Examinee(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length =40)
    regnum = models.CharField(max_length=20)
    email = models.EmailField()
    exam_type = models.ForeignKey(ExamType)
    invigilator = models.ForeignKey('invigilator.Invigilator')
    dob = models.DateField(blank=True)
    intended = models.DateField(blank=True)
    approved = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
