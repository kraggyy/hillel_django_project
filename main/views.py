from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView

from main.forms import ContactForm
from main.tasks import send_contact_form


class MainView(FormView):
    template_name = 'main/index.html'
    form_class = ContactForm
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        send_contact_form.delay(form.cleaned_data['email'],
                                form.cleaned_data['text'])
        messages.success(self.request, 'Your email has been send!')
        return super(MainView, self).form_valid(form)
