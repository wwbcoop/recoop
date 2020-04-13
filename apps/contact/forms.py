# django
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.core.mail import send_mail
from django.conf import settings
# contrib
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3


class ContactFormDev(forms.Form):
    """ Contact form """

    name = forms.CharField(
        label = _('Nombre')
    )
    subject = forms.CharField(
        label = _('Asunto')
    )
    email = forms.EmailField(
        label = _('Correo electrónico')
    )
    message = forms.CharField(
        label = _('Mensaje'),
        widget = forms.Textarea
    )

    def send_email(self):
        # send notification to contact sender
        send_mail(
            _(
                'Hemos recibido un mensaje de contacto en coop.re'
            ),
            '\n'.join([
                'De: %s <%s>' % ( self.cleaned_data['name'], self.cleaned_data['email']),
                'Asunto: %s' % self.cleaned_data['subject'],
                'Cuerpo: %s' % self.cleaned_data['message'],
                'Este es un mensaje automático, no lo respondas!'
            ]),
            'no-reply@coop.re',
            [ self.cleaned_data['email'] ],
            fail_silently=False,
        )
        # send notifications to site admins
        recipients = [ i[1] for i in settings.ADMINS ]
        send_mail(
            _('Ha habido un nuevo correo de contacto en ' + settings.DOCUMENT_TITLE),
            '\n'.join([
                'De: %s <%s>' % ( self.cleaned_data['name'], self.cleaned_data['email']),
                'Asunto: %s' % self.cleaned_data['subject'],
                'Cuerpo: %s' % self.cleaned_data['message'],
            ]),
            'no-reply@coop.re',
            recipients,
            fail_silently=False,
        )

class ContactForm(ContactFormDev):

    captcha = ReCaptchaField(widget=ReCaptchaV3)
