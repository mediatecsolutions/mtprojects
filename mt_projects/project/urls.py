from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^new/$', 'mt_projects.project.views.new_project'),
    url(r'^(?P<project_id>[^/]+)/$', 'mt_projects.project.views.project'),
    url(r'^(?P<project_id>[^/]+)/edit/$', 'mt_projects.project.views.edit_project'),
    url(r'^(?P<project_id>[^/]+)/todo/add/$', 'mt_projects.project.views.add_todo'),
    url(r'^(?P<project_id>[^/]+)/todo/(?P<todo_id>[^/]+)/delete/$', 'mt_projects.project.views.delete_todo'),
    url(r'^(?P<project_id>[^/]+)/todo/(?P<todo_id>[^/]+)/edit/$', 'mt_projects.project.views.edit_todo'),
    url(r'^', 'mt_projects.project.views.projects'),
)
