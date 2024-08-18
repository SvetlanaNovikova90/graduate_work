from django.contrib import admin

from clinic.models import Doctor, Service, Department, Carousel, Contact

admin.site.register(Doctor)

admin.site.register(Service)

admin.site.register(Department)

admin.site.register(Carousel)

admin.site.register(Contact)
