from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    
    
    
    url(r'^auth/', include('loginsys.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('article.urls')),
)
