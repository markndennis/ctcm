from django.conf.urls import patterns, include, url
from exams import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ctcm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    
    url(r'^createexamtype$','exams.tests.createexamtype', name='testexamtype'),
    
)