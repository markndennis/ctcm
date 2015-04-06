from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from invigilator.models import Invigilator
from django.views import generic


# Create your views here.

def home(request):
    context = {'title' : 'Invigilator Home'}
    return render(request, 'invigilator/home.html', context)
    
    
# class invigilator_list(generic.ListView):
#     model = Invigilator
#     template_name = 'invigilator/invigilatorList.html'
   
def invigilator_list(request):
    invig_list = Invigilator.objects.order_by('institution')
    #invig_list = Invigilator.objects.all()
    context = {'invigilator_list':invig_list,'title':'Invigilator List'}
    return render(request, 'invigilator/invigilatorList.html', context)
    
def invigilator_detail(request, invig_id):
    thisinvigilator = get_object_or_404(Invigilator, pk=invig_id)
    title = 'Invigilator ' + thisinvigilator.first_name + " " + thisinvigilator.last_name+ ' Details'
    context = {'invigilator':thisinvigilator, 'title':title}
    return render(request, 'invigilator/detail.html', context)    

        

     