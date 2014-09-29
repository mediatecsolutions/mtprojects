from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mt_online.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', 'mt_projects.note.views.note'),
)
