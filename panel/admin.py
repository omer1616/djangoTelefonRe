from django.contrib import admin
from .models import Person, Company, PersonCall


# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "is_active", "company")


admin.site.register(Person, PersonAdmin)
admin.site.register(Company)


class PersonCallAdmin(admin.ModelAdmin):
    list_display = ("name", "description", 'choices_call_type')


admin.site.register(PersonCall, PersonCallAdmin)
