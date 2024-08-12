from django.shortcuts import render
from django.views.generic import ListView

from clinic.models import Doctor


class DoctorListView(ListView):
    model = Doctor
    template_name = "clinic/doctor_list.html"
