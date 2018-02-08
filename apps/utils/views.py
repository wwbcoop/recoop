# django
from django.shortcuts import render
from django.utils.html import escape
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView

class PopupFormView(LoginRequiredMixin, FormView):

    def form_valid(self, form):
        instance = form.save()
        return HttpResponse('<script type="text/javascript">opener.dismissAddRelatedObjectPopup(window, "%s", "%s");</script>' % (\
                            escape(instance.id),
                            escape(instance.name)
        ))
