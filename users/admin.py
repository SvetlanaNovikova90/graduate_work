from django.contrib import admin

from users.models import User, Recording

admin.site.register(User)

admin.site.register(Recording)
