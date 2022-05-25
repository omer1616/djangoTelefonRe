from django.contrib import admin
from .models import Person, Company


# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "is_active", "company")


admin.site.register(Person, PersonAdmin)
admin.site.register(Company)
