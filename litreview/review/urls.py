from django.urls import path

from review.views import ReviewListView, ReviewDetailView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView

urlpatterns = [
    path('', ReviewListView.as_view(), name='review_list'),
    path('<int:pk>', ReviewDetailView.as_view(), name='review_detail'),
    path('new/', ReviewCreateView.as_view(), name='review_create'),
    path('edit/<int:pk>', ReviewUpdateView.as_view(), name='review_edit'),
    path('delete/<int:pk>', ReviewDeleteView.as_view(), name='review_delete'),
]