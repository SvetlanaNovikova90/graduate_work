from django.contrib import admin

from users.models import User, Recording


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email")


admin.site.register(Recording)
