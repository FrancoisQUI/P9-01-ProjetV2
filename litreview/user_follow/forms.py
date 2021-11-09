from pprint import pprint

from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import UserFollows


class NewFollowForm(ModelForm):

    class Meta:
        model = UserFollows
        fields = ['followed_user']

