from django.contrib import admin

from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'headline', 'user', 'time_created')
    list_filter = ['user']


admin.site.register(Review)
