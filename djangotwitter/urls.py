from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import twitter.urls
import mobile.urls

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(twitter.urls.urlpatterns)),
    url(r'^mobile', include(mobile.urls.urlpatterns)),
    #url(r'^$', 'twitter.views.say_hello'),
    # url(r'^$', include(twitter_patterns)),
)
