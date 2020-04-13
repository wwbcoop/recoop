# django
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy
from django.contrib import messages
# project
from .models import Initiative
from .forms import InitiativeForm, InitiativeFormDev
from django.conf import settings

class InitiativeCreate(CreateView):
    """ Project creation form in user dashboard. """

    model = Initiative
    form_class = InitiativeForm if not settings.DEBUG else InitiativeFormDev
    success_url = reverse_lazy('front')

    def form_valid(self, form):
        messages.success(self.request, _(
            'Tu iniciativa ha sido enviada a moderación. '
            'Gracias por tu interés, recibirás noticias en breve.'
        ))
        form.send_email()
        return super(InitiativeCreate, self).form_valid(form)
