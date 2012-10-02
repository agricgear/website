#encoding: utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from django.utils.translation import ugettext_lazy as _

from models import Contact
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('notified', )

    def clean(self):
        if not self.cleaned_data['phone'] and not self.cleaned_data['email']:
            raise forms.ValidationError(_(u'tienes que rellenar el email o el teléfono'))
        return self.cleaned_data

@csrf_exempt
def buy(request):
    ok = False
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            ok = True
    return render_to_response('buy.html', {
        'form': form,
        'ok': ok
    },
    context_instance=RequestContext(request)
    )

def video(request):
    #<iframe width="640" height="480" src="http://www.youtube.com/embed/albCTzEVraA" frameborder="0" allowfullscreen></iframe>
    video_embed = """
    <iframe width="920" height="550" src="http://www.youtube.com/embed/LwO7mkRfrM4" frameborder="0" allowfullscreen></iframe>
    """
    return render_to_response('content-video.html', {
        'video_embed': video_embed,
        'flatpage': {
            'title': 'Videos de Agroguía',
            'content': mark_safe("""<p>A continuación puede ver un video en el cual un agricultor trata una parcela con Agroguía. En ella aplica herbicida con una máquina Aguirre de 18 metros.</p>

                 <iframe width="480" height="360" src="http://www.youtube.com/embed/albCTzEVraA" frameborder="0" allowfullscreen></iframe>

<p>El video está dividido en dos partes, además se muestran diferentes cámaras; una externa que muestra el trabajo del tractor, una interna que recoge los comentarios del agricultor y por último una mostrando la pantalla de Agroguía.</p>
        
            <p>Puedes ver la segunda parte en <a href="http://www.youtube.com/watch?feature=player_embedded&v=TVRus8td5v0">youtube</a>.</p>
            """)
        }
    },
    context_instance=RequestContext(request)
    )
