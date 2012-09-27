from django.core.management.base import BaseCommand, CommandError

from web.models import Contact
from django.core.mail import send_mail
from django.conf import settings


class Command(BaseCommand):
    args = ''
    help = 'send notifications'


    def handle(self, *args, **options):
        for x in Contact.objects.filter(notified=False):
            try:
                t = """
                    name: %s
                    phone: %s
                    email: %s
                """ % (x.name, x.phone, x.email)
                send_mail('[Agroguia] web info', 
                    t,
                    settings.EMAIL_HOST_USER,
                    ['laura@agroguia.es', 'javi@agroguia.es'],
                    fail_silently=True)
                x.notified = True
                x.save()
            except:
                pass


