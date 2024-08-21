from django.test import TestCase, Client
from django.urls import reverse


from clinic.models import Doctor, Department, Service
from users.models import User, Recording


class ClinicTestCases(TestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@yandex.ru', password='password')
        self.doctor = Doctor.objects.create(name='Иванова Светлана')
        self.department = Department.objects.create(title='Кардиология')
        self.service = Service.objects.create(department=self.department, title='Диагностика', price='100')
        self.recording = Recording.objects.create(user=self.user, service=self.service, datetime_rec='2024-08-21 20:00')

    def test_departament_list(self):
        """Тест вывода списка отделений."""
        client = Client()
        url = reverse("clinic:department")
        response = client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEqual(Department.objects.all().count(), 1)

    def test_departament_detail(self):
        """Тест вывода информации об отделении."""
        client = Client()
        url = reverse("clinic:department_detail", args=(self.department.pk,))
        response = client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEqual(Department.objects.all().count(), 1)

    def test_doctor_list(self):
        """Тест вывода списка врачей."""
        client = Client()
        url = reverse("clinic:doctor")
        response = client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEqual(Doctor.objects.all().count(), 1)

    def test_doctor_detail(self):
        """Тест вывода информации о докторе."""
        client = Client()
        url = reverse("clinic:doctor_detail", args=(self.doctor.pk,))
        response = client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEqual(Doctor.objects.all().count(), 1)

