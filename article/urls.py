from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    url(r'^articles/all/$', 'article.views.articles', name='list'),
    url(r'^articles/addlike/(?P<article_id>\d+)/$', 'article.views.addlike'),
    url(r'^articles/addcom/(?P<article_id>\d+)/$', 'article.views.addcom'),

    url(r'^articles/get/(?P<article_id>\d+)/$', 'article.views.article'),
    url(r'^About/', 'article.views.about', name='about'),
    url(r'^$', 'article.views.articles', name='list'),
   # url(r'^tempview', 'article.views.tempview'),
    #url(r'^easy', 'article.views.tempview2'),

 	 
    #url(r'^', 'article.views.articles'),
    #
    )
