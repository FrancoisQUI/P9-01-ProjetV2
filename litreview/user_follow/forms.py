from django.forms import ModelForm

from .models import UserFollows


class NewFollowForm(ModelForm):

    class Meta:
        model = UserFollows
        fields = ['followed_user']
