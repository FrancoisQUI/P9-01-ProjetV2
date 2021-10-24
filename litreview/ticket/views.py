from django import forms
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from ticket.models import Ticket


class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    login_url = ''
    redirect_field_name = 'redirect_to'
    context_object_name = "tickets"


class TicketDetailView(LoginRequiredMixin, DetailView):
    model = Ticket
    login_url = ''
    redirect_field_name = 'redirect_to'
    context_object_name = "ticket"


class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    fields = ['title', 'description', 'image']
    login_url = ''
    redirect_field_name = 'redirect_to'
    context_object_name = "ticket"

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

    class Meta:
        widgets = {'image': forms.ImageField()}


class TicketUpdateView(LoginRequiredMixin, UpdateView):
    model = Ticket
    fields = ['title', 'description', 'image']
    login_url = ''
    redirect_field_name = 'redirect_to'
    context_object_name = "ticket"

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)


class TicketDeleteView(LoginRequiredMixin, DeleteView):
    model = Ticket
    success_url = reverse_lazy('post')
    login_url = ''
    redirect_field_name = 'redirect_to'
    context_object_name = "ticket"
