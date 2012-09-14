from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'', include('web.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('django.contrib.flatpages.urls')),
)
"""
urlpatterns += i18n_patterns('',
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'home-gps.html'}, name='home'),
    url(_(r'^pc-gps-workout'), 'django.views.generic.simple.direct_to_template', {'template': 'home-pc.html'},  name='home-pc')
)
"""
