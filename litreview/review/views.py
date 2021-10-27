from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from review.forms import ReviewCreateForm, ReviewUpdateForm
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
    form_class = ReviewCreateForm
    template_name = 'review/review_create_form.html'
    login_url = ''
    redirect_field_name = 'redirect_to'
    context_object_name = "review"

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)


class ReviewUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewUpdateForm
    template_name = 'review/review_update_form.html'
    login_url = ''
    redirect_field_name = 'redirect_to'
    context_object_name = "review"

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

    def test_func(self):
        self.object = self.get_object()
        return self.object.user == self.request.user


class ReviewDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Review
    success_url = reverse_lazy('review_list')
    login_url = ''
    redirect_field_name = 'redirect_to'
    context_object_name = "review"

    def test_func(self):
        self.object = self.get_object()
        return self.object.user == self.request.user