from django.contrib import admin

from accounts.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'profile_picture', 'id')
    list_filter = ('profile_picture', )


admin.site.register(UserProfile, UserProfileAdmin)


