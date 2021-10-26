from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

from review.models import Review


class ReviewListView(LoginRequiredMixin, ListView):
    model = Review
    login_url = ''
    redirect_field_name = 'redirect_to'
    context_object_name = "reviews"


class ReviewDetailView(LoginRequiredMixin, DetailView):
    model = Review
    login_url = ''
    redirect_field_name = 'redirect_to'
    context_object_name = "review"


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['rating', 'headline', 'body']
    login_url = ''
    redirect_field_name = 'redirect_to'
    context_object_name = "review"

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

    class Meta:
        widget = {'rating': forms.RadioSelect()}
