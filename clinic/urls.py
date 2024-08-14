from django.urls import path
from django.views.generic import TemplateView

from clinic.apps import ClinicConfig
from clinic.views import DoctorListView, ProductsDetailView, CarouselListView
from users.apps import UsersConfig

app_name = ClinicConfig.name
urlpatterns = [
    path("", CarouselListView.as_view(), name='home'),
    path("doctor_list/", DoctorListView.as_view(), name='doctor'),
    path("doctor/<int:pk>/", ProductsDetailView.as_view(), name='doctor_detail'),
    ]