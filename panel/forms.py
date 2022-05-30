from django.forms import ModelForm, TextInput, ModelChoiceField
from panel.models import Person, PersonCall, Company


class ContactCompany(ModelForm):
    class Meta:
        model = Company
        fields = ["name", "company_description"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'input',
            }),
            "company_description": TextInput(attrs={
                'class': 'input',
            }),

        }


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


class ContactPersonCall(ModelForm):
    class Meta:
        model = PersonCall
        fields = ["name", "description", "choices_call_type"]
        widgets = {
            "description": TextInput(attrs={
                'class': 'input',
            }),

        }
