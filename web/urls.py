from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'home-gps.html'}, name='home'),
    url(_(r'^agroguia-pc'), 'django.views.generic.simple.direct_to_template', {'template': 'home-pc.html'},  name='home-pc'),
    url(_(r'^comprar-guiado-gps'), 'django.views.generic.simple.direct_to_template', {'template': 'buy.html'},  name='home-buy')
)
