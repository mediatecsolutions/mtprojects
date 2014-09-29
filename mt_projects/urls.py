from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^note/', include('mt_projects.note.urls')),
    url(r'^project/', include('mt_projects.project.urls')),
    url(r'^quote/', include('mt_projects.quote.urls')),
    url(r'^todo/', include('mt_projects.todo.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^login/', 'mt_projects.user_auth.views.login_view'),
    url(r'^logout/', 'mt_projects.user_auth.views.logout_view'),
    url(r'^', 'mt_projects.project.views.schedule'),
)
