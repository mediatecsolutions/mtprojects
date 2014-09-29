from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mt_online.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^add/$', 'mt_projects.todo.views.add'),
    url(r'^(?P<todo_id>[^/]+)/edit/$', 'mt_projects.todo.views.edit'),
    url(r'^(?P<todo_id>[^/]+)/finish/$', 'mt_projects.todo.views.finish'),
    url(r'^(?P<todo_id>[^/]+)/reopen/$', 'mt_projects.todo.views.reopen'),
    url(r'^(?P<todo_id>[^/]+)/delete/$', 'mt_projects.todo.views.delete'),
    url(r'^', 'mt_projects.todo.views.todo'),
)
