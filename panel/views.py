from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect ,JsonResponse
from panel.models import Person, Company
from panel.forms import ContactPerson
from django.contrib import  messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    form = ContactPerson(request.POST or None)
    if form.is_valid():
        person = form.save()
        return HttpResponseRedirect(person.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, "index.html", context)


def list(request):
    context = {
        "persons": Person.objects.all()
    }

    return render(request, "list.html", context)


def list_details(request, id):
    person = get_object_or_404(Person, id=id)
    return render(request, "list-details.html", {
        "person": person
    })


def navbar(request):
    return render(request, "navbar.html")


def sidebar(request):
    return render(request, "sidebar.html")


def update(request, id):
    person = get_object_or_404(Person, id=id)
    form = ContactPerson(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        messages.success(request,  "ilk mesajınız olusturuldu")
        return HttpResponseRedirect(person.get_absolute_url())
    context = {
        'person':  person,

    }

    return render(request, "update.html", context)

@csrf_exempt
def delete(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return JsonResponse({'success': True})
