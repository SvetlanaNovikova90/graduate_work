from django.shortcuts import render
from django.views.generic import ListView, DetailView

from clinic.models import Doctor


class DoctorListView(ListView):
    model = Doctor
    template_name = "clinic/doctor_list.html"


class ProductsDetailView(DetailView):
    model = Doctor
    template_name = "clinic/doctor_detail.html"
