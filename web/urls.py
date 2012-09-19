from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _

from views import buy

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'home-gps.html'}, name='home'),
    url(r'^gps-agricola$', 'django.views.generic.simple.direct_to_template', {'template': 'home-gps.html'}, name='home'),
    url(r'^guiado-gps$', 'django.views.generic.simple.direct_to_template', {'template': 'home-gps.html'}, name='home'),
    url(_(r'^agroguia-pc'), 'django.views.generic.simple.direct_to_template', {'template': 'home-pc.html'},  name='home-pc'),
    url(_(r'^comprar-guiado-gps'), buy,  name='home-buy'),
    url(_(r'^nosotros'), 'django.views.generic.simple.direct_to_template', {'template': 'about.html'},  name='about'),
)

# legacy 
urlpatterns += patterns('',
    url(_(r'^nosotros'), 'django.views.generic.simple.direct_to_template', {'template': 'about.html'},  name='about'),
    url(_(r'^comprar-agroguia'), 'django.views.generic.simple.redirect_to', {'url' : _('/comprar-guiado-gps')}),

    url(r'^gps-agricola-videos', 'django.views.generic.simple.redirect_to', {'url' : _('/es/gps-agricola-videos')}),
    url(r'^gps-agricola-caracteristicas', 'django.views.generic.simple.redirect_to', {'url' : _('/es/gps-agricola-caracteristicas')}),
    url(r'^utilidades-gps-agricultura', 'django.views.generic.simple.redirect_to', {'url' : _('/es/utilidades-gps-agricultura')}),
    url(r'^parcelas-agroguia-sigpac', 'django.views.generic.simple.redirect_to', {'url' : _('/es/parcelas-agroguia-sigpac')}),
    url(r'^medir-parcelas-gps', 'django.views.generic.simple.redirect_to', {'url' : _('/es/medir-parcelas-gps')}),
    url(r'^guiado-agricultura-simple', 'django.views.generic.simple.redirect_to', {'url' : _('/es/guiado-agricultura-simple')}),
    url(r'^gps-herbicida-abono', 'django.views.generic.simple.redirect_to', {'url' : _('/es/gps-herbicida-abono')}),
    url(r'^gps-agricola-sencillo-usar', 'django.views.generic.simple.redirect_to', {'url' : _('/es/gps-agricola-sencillo-usar')}),
    url(r'^informacion-agroguia$', 'django.views.generic.simple.redirect_to', {'url' : _('/comprar-guiado-gps')}),
    url(r'^informacion-guiado-gps$', 'django.views.generic.simple.redirect_to', {'url' : _('/comprar-guiado-gps')}),
)




# done
#('/','/%s/%s/index' % main),    # homepage
   #('^/informacion-guiado-gps$', '/%s/%s/askinfo' % main),
   #('^/informacion-agroguia$', '/%s/%s/post/4' % main),
   #('^/gps-agricola$', '/%s/%s/index' % main),
   #('^/guiado-gps$', '/%s/%s/index' % main),
   #('^/$', '/%s/%s/index' % main),
   #('^/comprar-agroguia$', '/%s/%s/buy' % main),
    #^/gps-agricola-sencillo-usar$#post/1
    #^/gps-herbicida-abono$#post/2
    #^/guiado-agricultura-simple$#post/3
    #^/medir-parcelas-gps$#post/5
    #^/parcelas-agroguia-sigpac$#post/6
    #^/utilidades-gps-agricultura$#post/7
    #^/gps-agricola-caracteristicas$#post/8
    #^/gps-agricola-videos$#post/9
#*   ^/comprar-gps-agricola$#post/4
#*   ^/nosotros$#post/10 
#
