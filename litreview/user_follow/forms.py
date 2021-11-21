from django.forms import ChoiceField, Form


class NewFollowForm(Form):

    def __init__(self, *args, choices, **kwargs):
        super(NewFollowForm, self).__init__(*args, **kwargs)
        self.fields['followed_user_pk'] = ChoiceField(choices=choices)

    class Meta:
        fields = ['followed_user_pk']

