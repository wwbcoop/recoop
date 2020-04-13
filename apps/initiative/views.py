# django
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy
# project
from .models import Initiative
from .forms import InitiativeForm


class InitiativeCreate(CreateView):
    """ Project creation form in user dashboard. """

    model = Initiative
    form_class = InitiativeForm
    success_url = reverse_lazy('front')

    def form_valid(self, form):
        messages.success(self.request, _(
        'Tu iniciativa ha sido enviada a moderación. '
        'Gracias por tu interés, recibirás noticias en breve.'
        ))
        return super(InitiativeCreate, self).form_valid(form)
