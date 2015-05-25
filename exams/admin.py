from django.contrib import admin
from exams.models import ExamType

#Register your models here.

class ExamTypeAdmin(admin.ModelAdmin):
    #fields = [ 'last_name','first_name', 'email']
    list_display = ('exam_type','pk')    
    
admin.site.register(ExamType,ExamTypeAdmin)