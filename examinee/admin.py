from django.contrib import admin
from examinee.models import Examinee
#from exams.models import ExamType

# Register your models here.

class ExamineeAdmin(admin.ModelAdmin):
    #fields = [ 'last_name','first_name', 'email']
    list_display = ('last_name', 'first_name','dob','intended','invigilator','pk')
    
    
class ExamTypeAdmin(admin.ModelAdmin):
    #fields = [ 'last_name','first_name', 'email']
    list_display = ('exam_type','pk')    
    
admin.site.register(Examinee, ExamineeAdmin)



