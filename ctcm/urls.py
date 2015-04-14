from django.conf.urls import patterns, include, url
from django.contrib import admin, auth
from django.contrib.auth import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ctcm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^', include('django.contrib.auth.urls')), # this automatically includes patters for login, logout etc.
    url(r'^examinee/',include('examinee.urls', namespace='examinee')),
    url(r'^invigilator/',include('invigilator.urls', namespace = 'invigilator')),
    url(r'^$','ctcm.views.welcome', name='welcome'),
    url(r'^about$','ctcm.views.about', name='about'),
    url(r'^login/$',auth.views.login,{'extra_context':{'title':'login'}},name='login'),
    url(r'^logout/$',auth.views.logout,name='logout'),
    #url(r'^mylogin/$','ctcm.views.mylogin', name='mylogin'),
    #url(r'^listexaminees$','examinee.views.listexaminees', name='listexaminees'),
)
