from django.forms import ModelForm, RadioSelect

from review.models import Review


class ReviewCreateForm(ModelForm):
    class Meta:
        model = Review
        fields = ["ticket", "rating", "headline", "body"]
        widgets = {"rating": RadioSelect()}


class ReviewUpdateForm(ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "headline", "body"]
        widgets = {"rating": RadioSelect()}


class ReviewFormFromTicket(ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "headline", "body"]
        widgets = {"rating": RadioSelect()}



