from pprint import pprint

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.contrib.auth.decorators import login_required

from .forms import NewFollowForm
from .models import UserFollows


@login_required
def manage_follow_view(request):
    context = {}
    user = request.user
    user_pk = request.user.id
    follows_pk = [user_follow.followed_user.id for user_follow in UserFollows.objects.filter(user_id=user_pk)]
    follows = UserFollows.objects.filter(user_id=user_pk)
    followers = UserFollows.objects.filter(followed_user_id=user_pk)
    choices = User.objects.all().exclude(pk=user_pk)\
        .exclude(pk__in=follows_pk)\
        .values_list("pk", "username")

    pprint(choices)

    form = NewFollowForm(request.POST, choices=choices)

    if request.method == 'POST':
        pprint(request.POST)
        followed_user_pk = request.POST.get('followed_user_pk')
        followed_user = User.objects.get(pk=followed_user_pk)
        follows = UserFollows.objects.filter(user_id=user_pk)
        followers = UserFollows.objects.filter(followed_user_id=user_pk)
        if form.is_valid():
            try:
                follow = UserFollows.objects. \
                    create(user=user, followed_user=followed_user)
                follow.save()
                return redirect('follows')
            except IntegrityError:
                context['error_message'] = \
                    f'Vous suivez déjà cette personne : {followed_user}'

    context["follows"] = follows
    context["followers"] = followers
    context["form"] = form

    return render(request, 'user_follow/subs_view.html', context)


class UserFollowsDeleteView(LoginRequiredMixin, DeleteView):
    model = UserFollows
    success_url = reverse_lazy('follows')
