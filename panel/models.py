from django.db import models

# Create your models here.
from django.db import models

from django.urls import reverse


class Company(models.Model):
    name = models.CharField(max_length=150, verbose_name="Firma Adı")
    company_description = models.TextField(max_length=500, verbose_name="Açıklama")

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):

    name = models.CharField(max_length=150, verbose_name="İsim Soyisim")
    phone_number = models.CharField(max_length=50, verbose_name="Telefon Numarası")
    description = models.TextField(verbose_name="Açıklama")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Firma")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('list-details', kwargs={'id': self.id})


class PersonCall(models.Model):
    name = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name="İsim Soyisim")
    description = models.TextField(max_length=500, verbose_name="Açıklma")

    CALL_TYPE = [
        ("gelen", "gelen"),
        ("giden", "giden"),
    ]
    choices_call_type = models.CharField(
        max_length=5,
        choices=CALL_TYPE,
        verbose_name="Arama Türü"

    )
