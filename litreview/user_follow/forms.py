from pprint import pprint

from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import UserFollows


class NewFollowForm(ModelForm):

    # def __init__(self, user=None, user_follows=None, *args, **kwargs):
    #     pprint(user)
    #     super().__init__(user, user_follows, *args, **kwargs)
    #     self.fields['followed_user'].queryset = User.objects.exclude(id=user)

    class Meta:
        model = UserFollows
        fields = ['followed_user']

