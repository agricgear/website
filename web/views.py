#encoding: utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from django.utils.translation import ugettext_lazy as _

from models import Contact
from django.views.decorators.csrf import csrf_exempt

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact

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
