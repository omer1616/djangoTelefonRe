from django.db import models

# Create your models here.
from django.db import models

from django.urls import reverse


# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)
    description = models.TextField()
    company = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('list-details', kwargs={'id': self.id})

    # def get_absolute_list(self):
    #     from django.urls import reverse
    #     return reverse('list')


class Company(models.Model):
    name = models.CharField(max_length=150)


class PersonCall(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    CALL_TYPE = [
        ("gelen", "gelen"),
        ("giden", "giden"),
    ]

    choices_call_type = models.CharField(
        max_length=5,
        choices=CALL_TYPE,

    )


