{"changed":true,"filter":false,"title":"views.py","tooltip":"/ctcm/views.py","value":"from django.shortcuts import render\nfrom django.http import HttpResponse\n#from django.template.response import TemplateResponse\nfrom django.core.mail import send_mail\nfrom django.contrib.auth import views\nfrom django.template.response import TemplateResponse\n\n\n# Create your views here.\n\ndef welcome(request):\n    context = {'title' : 'Welcome'}\n    return render(request, 'welcome.html', context)\n    \ndef about(request):\n    context = {'title' : 'About'}\n    return render(request, 'about.html', context)\n    \n# def mylogin(request):\n#     template_response = views.login(request)\n#     template_response.context={'myvar':'myvar content'}\n#     return template_response\n#     #return render(request, 'registration/login.html',context)\n    \ndef mail(to,cc,subject,message):\n    mailfrom = \"markndennis@hotmail.com\"\n    send_mail(subject, message, mailfrom, [to], fail_silently=False)\n    return","undoManager":{"stack":[],"mark":-1,"position":-1},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":8,"column":25},"end":{"row":8,"column":25},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1432589113000}