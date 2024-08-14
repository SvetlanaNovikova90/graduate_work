from django.db import models

NULLABLE = {"blank": True, "null": True}


class Carousel(models.Model):
    title = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(**NULLABLE, verbose_name="Описание")
    image_ph = models.ImageField(
        upload_to="carousel/", **NULLABLE, verbose_name="Изображение"
    )


    def __str__(self):
        return f"{self.title}"


class Doctor(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО врача")
    description = models.TextField(**NULLABLE, verbose_name="Описание")
    image_ph = models.ImageField(
        upload_to="doctor/", **NULLABLE, verbose_name="Изображение"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "врач"
        verbose_name_plural = "врачи"


class Department(models.Model):
    title = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(**NULLABLE, verbose_name="Описание")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "отделение"
        verbose_name_plural = "отделения"


class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(**NULLABLE, verbose_name="Описание")
    doctor = models.ForeignKey(
        "Doctor",
        **NULLABLE,
        on_delete=models.SET_NULL,
        verbose_name="Врач",
    )
    department = models.ForeignKey(
        "Department",
        **NULLABLE,
        on_delete=models.SET_NULL,
        verbose_name="отделение",
    )
    price = models.IntegerField(verbose_name="Цена за услугу")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "услуга"
        verbose_name_plural = "услуги"
