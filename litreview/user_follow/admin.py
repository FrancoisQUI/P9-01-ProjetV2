from django.contrib import admin

from .models import UserFollows


class UserFollowsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'followed_user')
    list_filter = ['user']


admin.site.register(UserFollows, UserFollowsAdmin)
