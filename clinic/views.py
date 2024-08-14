from django.shortcuts import render
from django.views.generic import ListView, DetailView

from clinic.models import Doctor, Carousel, Department, Service
from clinic.services import get_cached_subjects_for_service


class CarouselListView(ListView):
    model = Carousel
    template_name = "clinic/index.html"


class DoctorListView(ListView):
    model = Doctor
    template_name = "clinic/doctor_list.html"


class ProductsDetailView(DetailView):
    model = Doctor
    template_name = "clinic/doctor_detail.html"


class DepartmentListView(ListView):
    model = Department
    template_name = "clinic/department_list.html"


class DepartmentDetailView(DetailView):
    model = Department
    template_name = "clinic/department_detail.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        context_data['services'] = get_cached_subjects_for_service(self.object.pk)
        return context_data
