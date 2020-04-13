# django
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
# project
from .forms import ContactForm, ContactFormDev
from django.conf import settings

class ContactView(FormView):

    form_class = ContactFormDev if settings.DEBUG else ContactForm
    success_url = reverse_lazy('front')

    def form_valid(self, form):
        form.send_email()
        messages.success(
            self.request,
            _(
                'Gracias por tu mensaje, te contestaremos con la '
                'mayor brevedad'
            )
        )
        return super().form_valid(form)
