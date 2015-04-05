from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ctcm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^examinee/',include('examinee.urls', namespace='examinee')),
    url(r'^invigilator/',include('invigilator.urls', namespace = 'invigilator')),
    url(r'^$','ctcm.views.welcome', name='welcome'),
    url(r'^about$','ctcm.views.about', name='about'),
)
