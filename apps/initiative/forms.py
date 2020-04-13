# django
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
# contrib
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
# project
from .models import Initiative
from django.conf import settings


class InitiativeFormDev(forms.ModelForm):
    class Meta:
        model = Initiative
        fields = [
            'name',
            'summary',
            'domain',
            'ip',
            'email',
        ]

    def send_email(self):
        # send notification to contact sender
        send_mail(
            _(
                'Has solicitado un dominio en %s. '
            ),
            _(
                'Has solicitado un dominio en coop.re '
                'Gracias por tu solicitud. Recibirás respuesta tan pronto '
                'como sea posible. '
                'Este es un correo automático, no lo respondas '
            ),
            'no-reply@coop.re',
            [ self.cleaned_data['email'] ],
            fail_silently=False,
        )
        # send notifications to site admins
        recipients = [ i[1] for i in settings.ADMINS ]
        send_mail(
            _('Ha habido una nueva solicitud en ' + settings.DOCUMENT_TITLE),
            '\n'.join([
                'De: %s' % self.cleaned_data['email'],
                'Nombre: %s' % self.cleaned_data['name'],
                'Descripción: %s' % self.cleaned_data['summary'],
                'Dominio: %s' % self.cleaned_data['domain'],
                'IP: %s' % self.cleaned_data['ip'],
            ]),
            'no-reply@coop.re',
            recipients,
            fail_silently=False,
        )

class InitiativeForm(InitiativeFormDev):

    captcha = ReCaptchaField(widget=ReCaptchaV3)
