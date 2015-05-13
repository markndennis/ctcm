from django.conf.urls import patterns, include, url
from invigilator import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ctcm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'invigilator.views.home', name='home'),
    #url(r'^invigilatorList$',views.invigilator_list.as_view(), name='invigilatorList'),
    url(r'^invigilatorList/(?P<so>)$','invigilator.views.invigilator_list.so', name='invigilatorList'),
    url(r'^(?P<invig_id>\d+)/$','invigilator.views.invigilator_detail', name='invigilatorDetail'),
    
)
