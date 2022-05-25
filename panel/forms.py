from django.forms import ModelForm,  TextInput
from panel.models import Person


class ContactPerson(ModelForm):
    class Meta:
        model = Person
        fields = ["name", "phone_number", "description", 'company']
        widgets = {
            "name": TextInput(attrs={
                'class': 'input',
            }),
            "description": TextInput(attrs={
                'class': 'input',
            }),
            "phone_number": TextInput(attrs={
                'class': 'input',
            }),
            "company": TextInput(attrs={
                'class': 'input',
            }),
        }