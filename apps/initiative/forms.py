# django
from django import forms
# contrib
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
# project
from .models import Initiative


class InitiativeForm(forms.ModelForm):

    captcha = ReCaptchaField(widget=ReCaptchaV3)

    class Meta:
        model = Initiative
        fields = [
            'name',
            'summary',
            'domain',
            'ip',
            'email',
            'captcha'
        ]
