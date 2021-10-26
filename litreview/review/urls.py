from django.urls import path

from review.views import ReviewListView

urlpatterns = [
    path('', ReviewListView.as_view(), name='review_list'),
]