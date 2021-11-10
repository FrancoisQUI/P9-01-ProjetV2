from itertools import chain

from django.shortcuts import render
from django.db.models import CharField, Value

from review.models import Review
from ticket.models import Ticket


def my_posts_view(request):
    user = request.user

    reviews = Review.objects.filter(user=user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    tickets = Ticket.objects.filter(user=user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )

    return render(request,
                  template_name='my_posts/my_posts.html',
                  context={'posts': posts})
