from django.urls import path

from .views import manage_follow_view, UserFollowsDeleteView

urlpatterns = [
    path('', manage_follow_view, name='follows'),
    path('delete/<int:pk>', UserFollowsDeleteView.as_view(), name='follows_delete')
]