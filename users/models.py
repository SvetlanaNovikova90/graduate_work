from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    phone = models.CharField(max_length=35, **NULLABLE, verbose_name='Телефон')
    token = models.CharField(max_length=100, verbose_name='Token', **NULLABLE)
    verification_code = models.CharField(max_length=50, verbose_name='код верификации email', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"


class Recording(models.Model):
    user = models.ForeignKey(
        "User",
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Клиент",
    )
    service = models.ForeignKey(
        "clinic.Service",
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Услуга",
    )
    doctor = models.ForeignKey(
        "clinic.Doctor",
        **NULLABLE,
        on_delete=models.SET_NULL,
        verbose_name="Врач",
    )
    datetime_rec = models.DateTimeField(verbose_name='дата приема')
    status = models.BooleanField(default=True, verbose_name='Активность')

    def __str__(self):
        return f'{self.service}: {self.datetime}'

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
