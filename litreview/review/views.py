from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

from review.forms import ReviewForm
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
    form_class = ReviewForm
    template_name = 'review/review_form.html'
    login_url = ''
    redirect_field_name = 'redirect_to'
    context_object_name = "review"

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

