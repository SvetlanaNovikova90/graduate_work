from django.urls import path
from django.views.generic import TemplateView

from clinic.apps import ClinicConfig
from clinic.views import DoctorListView
from users.apps import UsersConfig

app_name = ClinicConfig.name
urlpatterns = [
    path("", TemplateView.as_view(template_name='clinic/index.html'), name='home'),
    path("doctor_list/", DoctorListView.as_view(), name='doctor'),
    ]