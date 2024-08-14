from django.contrib import admin

from clinic.models import Doctor, Service, Department, Carousel

admin.site.register(Doctor)

admin.site.register(Service)

admin.site.register(Department)

admin.site.register(Carousel)
