from itertools import chain

from django.shortcuts import render
from django.db.models import CharField, Value

from review.models import Review
from ticket.models import Ticket
from user_follow.models import UserFollows


def feed_view(request):
    user = request.user
    followed_users = list(UserFollows.objects.filter(user=user).values_list('followed_user', flat=True))

    reviews = Review.objects.filter(user__in=followed_users)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    reviews_from_my_tickets = Review.objects.filter(ticket__user=user)
    reviews_from_my_tickets = reviews_from_my_tickets.annotate(content_type=Value('REVIEW', CharField()))

    tickets = Ticket.objects.filter(user__in=followed_users)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    posts = sorted(
        chain(reviews, reviews_from_my_tickets, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )

    # remove duplicates
    posts = list(dict.fromkeys(posts))

    return render(request, template_name='feed/feed.html', context={'posts': posts, 'followed_users': followed_users})