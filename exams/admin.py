from django.contrib import admin
from exams.models import ExamType, Questions

#Register your models here.

class ExamTypeAdmin(admin.ModelAdmin):
    #fields = [ 'last_name','first_name', 'email']
    list_display = ('exam_type','pk')  
    
class QuestionsAdmin(admin.ModelAdmin):
    #fields = ['qnum','qtext']
    list_display = ('qnum','qtext','r1','r2','r3','r4','qtext_c','pk')
    
admin.site.register(ExamType,ExamTypeAdmin)
admin.site.register(Questions,QuestionsAdmin)