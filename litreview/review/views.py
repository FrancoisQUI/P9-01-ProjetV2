from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from review.forms import ReviewCreateForm, ReviewUpdateForm, ReviewFormFromTicket
from review.models import Review
from ticket.forms import TicketForm
from ticket.models import Ticket



class ReviewListView(LoginRequiredMixin, ListView):
    model = Review
    login_url = 'home'
    redirect_field_name = 'redirect_to'
    context_object_name = "reviews"


class ReviewDetailView(LoginRequiredMixin, DetailView):
    model = Review
    login_url = 'home'
    redirect_field_name = 'redirect_to'
    context_object_name = "review"


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewCreateForm
    template_name = 'review/review_create_form.html'
    login_url = 'home'
    redirect_field_name = 'redirect_to'
    context_object_name = "review"

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)


class ReviewUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewUpdateForm
    template_name = 'review/review_update_form.html'
    login_url = 'home'
    redirect_field_name = 'redirect_to'
    context_object_name = "review"

    def get_context_data(self, *args, **kwargs):
        context = super(ReviewUpdateView, self).get_context_data(*args, **kwargs)
        context['show_ticket_only'] = True
        return context

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

    def test_func(self):
        self.object = self.get_object()
        return self.object.user == self.request.user


class ReviewDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Review
    success_url = reverse_lazy('review_list')
    login_url = 'home'
    redirect_field_name = 'redirect_to'
    context_object_name = "review"

    def test_func(self):
        self.object = self.get_object()
        return self.object.user == self.request.user


def new_review_and_ticket(request):
    if request.method == "POST":
        try:
            ticket_id = request.POST.get('ticket')
            ticket = Ticket.objects.get(pk=ticket_id)
        except ObjectDoesNotExist:
            user = request.user
            title = request.POST.get('title')
            description = request.POST.get('description')
            image = request.POST.get('image')
            ticket_form = TicketForm(request.POST, request.FILES)
            if ticket_form.is_valid():
                ticket = Ticket.objects.create(title=title,
                                               description=description,
                                               image=image,
                                               user=user)
                ticket.save()
        rating = request.POST.get('rating')
        headline = request.POST.get('headline')
        body = request.POST.get('body')
        user = request.user
        form = ReviewUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            review = Review.objects.create(ticket=ticket,
                                           rating=rating,
                                           headline=headline,
                                           body=body,
                                           user=user)
            review.save()
            return redirect('feed')

    form = ReviewUpdateForm()
    ticket_form = TicketForm()

    return render(request=request,
                  template_name='review/review_and_ticket_create_form.html',
                  context={'form': form, 'ticket_form': ticket_form})


def new_review_from_ticket(request, ticket_id):
    context = {}
    ticket = Ticket.objects.get(pk=ticket_id)

    if request.method == "POST":
        rating = request.POST.get('rating')
        headline = request.POST.get('headline')
        body = request.POST.get('body')
        user = request.user
        form = ReviewFormFromTicket(request.POST)
        if form.is_valid():
            review = Review.objects.create(ticket=ticket,
                                           rating=rating,
                                           headline=headline,
                                           body=body,
                                           user=user)
            review.save()
            return redirect('feed')

    form = ReviewFormFromTicket()
    context['form'] = form
    context['ticket'] = ticket
    context['show_ticket_only'] = True

    return render(request=request,
                  template_name='review/review_create_form.html',
                  context=context)
