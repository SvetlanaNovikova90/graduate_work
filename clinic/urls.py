from django.urls import path
from django.views.generic import TemplateView

from clinic.apps import ClinicConfig
from clinic.views import DoctorListView, ProductsDetailView, CarouselListView, DepartmentListView, DepartmentDetailView, \
    ContactListView
from users.apps import UsersConfig

app_name = ClinicConfig.name
urlpatterns = [
    path("", CarouselListView.as_view(), name='home'),
    path("doctor_list/", DoctorListView.as_view(), name='doctor'),
    path("doctor/<int:pk>/", ProductsDetailView.as_view(), name='doctor_detail'),
    path("department_list/", DepartmentListView.as_view(), name='department'),
    path("department/<int:pk>/", DepartmentDetailView.as_view(), name='department_detail'),
    path("contact/", ContactListView.as_view(), name='contact'),
    ]