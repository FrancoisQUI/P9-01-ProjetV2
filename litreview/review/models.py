from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from ticket.models import Ticket


class Review(models.Model):
    ticket: Ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)),
        default=3,
    )
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    user: User = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk} - {self.ticket.title} - {self.user.username}"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('review_detail', kwargs={'pk': self.pk})
