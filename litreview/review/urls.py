from django.urls import path

from review.views import ReviewListView, ReviewDetailView, \
    ReviewCreateView, ReviewUpdateView, ReviewDeleteView, \
    new_review_from_ticket, new_review_and_ticket

urlpatterns = [
    path('', ReviewListView.as_view(), name='review_list'),
    path('<int:pk>', ReviewDetailView.as_view(), name='review_detail'),
    path('new/', ReviewCreateView.as_view(), name='review_create'),
    path('newwithticket/', new_review_and_ticket,
         name='create_review_and_ticket'),
    path('new/<int:ticket_id>', new_review_from_ticket,
         name='review_create_from_ticket'),
    path('edit/<int:pk>', ReviewUpdateView.as_view(), name='review_edit'),
    path('delete/<int:pk>', ReviewDeleteView.as_view(), name='review_delete'),
]
