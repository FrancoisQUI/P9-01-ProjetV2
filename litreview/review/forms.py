from django.forms import ModelForm, RadioSelect

from review.models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["ticket", "rating", "headline", "body"]
        widgets = {"rating": RadioSelect()}
