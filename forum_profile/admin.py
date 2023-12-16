from django.contrib import admin

# Register your models here.
from forum_profile.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    exclude = ['id']
    search_fields = ['username', 'description', 'signature', 'profile_color']
    list_display = ['username', 'photo', 'profile_color', 'user']
    list_editable = ['photo', 'profile_color']