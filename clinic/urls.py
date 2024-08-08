from django.urls import path
from django.views.generic import TemplateView

from clinic.apps import ClinicConfig
from users.apps import UsersConfig

app_name = ClinicConfig.name
urlpatterns = [
    path("", TemplateView.as_view(template_name='clinic/index.html'), name='home'),
    ]