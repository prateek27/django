from django.conf.urls import patterns, include, url
from django.contrib import admin
from login.views import get_name
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myfirstDjangoProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^get_name/', get_name),
    url(r'^admin/', include(admin.site.urls)),
)
