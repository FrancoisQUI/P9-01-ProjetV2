from django.urls import path

from .views import TicketListView, TicketDetailView, TicketCreateView, TicketUpdateView, TicketDeleteView

urlpatterns = [
    path('', TicketListView.as_view(), name='ticket_list'),
    path('<int:pk>/', TicketDetailView.as_view(), name='ticket_detail'),
    path('new/', TicketCreateView.as_view(), name='ticket_create'),
    path('edit/<int:pk>/', TicketUpdateView.as_view(), name='ticket_edit'),
    path('delete/<int:pk>/', TicketDeleteView.as_view(), name='ticket_delete'),
]