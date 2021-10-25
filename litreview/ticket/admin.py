from django.contrib import admin

from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'user', 'image', 'time_created')
    list_filter = ['user']


admin.site.register(Ticket, TicketAdmin)
