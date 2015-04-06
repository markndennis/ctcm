from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ctcm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'examinee.views.home', name='home'),
    url(r'^apply$', 'examinee.views.apply', name='apply'),
    url(r'^application$', 'examinee.views.application', name='application'),
    
)
