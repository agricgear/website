

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Contact(models.Model):
  date = models.DateTimeField(auto_now_add=True)
  name = models.CharField(_('name'), max_length=255)
  email = models.CharField(_('email'), max_length=255, null=True, blank=True)
  phone = models.CharField(_('phone'), max_length=255, null=True, blank=True)
  notified = models.BooleanField(default=False)
