from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, JsonResponse
from panel.models import Person, Company, PersonCall
from panel.forms import ContactPerson, ContactPersonCall,  ContactCompany
from django.contrib import messages
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
    # person_list = Person.objects.all()
    # query = request.GET.get('q')
    # if query:
    #     person_list = person_list.filter(title__icontains=query)
    return render(request, "list.html", context)


def search(request):
    from django.db.models import Q
    if request.method == "POST":
        searched = request.POST['searched']
        persons = Person.objects.filter(
            Q(company__contains=searched) | Q(name__contains=searched) | Q(phone_number__contains=searched))

        return render(request, "search_menu.html", {'searched': searched,
                                                    'persons': persons})


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
        messages.success(request, "ilk mesajınız olusturuldu")
        return HttpResponseRedirect(person.get_absolute_url())
    context = {
        'person': person,

    }

    return render(request, "update.html", context)


@csrf_exempt
def delete(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return JsonResponse({'success': True})


from django.urls import reverse


@csrf_exempt
def incoming_call(request):
    form = ContactPersonCall(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('incoming-call'))
    context = {
        'form': form,
    }
    return render(request, "incoming_call.html", context)


def outer_call(request):
    context = {
        "story_list": PersonCall.objects.all()
    }
    return render(request, "outer-call.html", context)


def add_company(request):
    company = ContactCompany(request.POST or None)
    if company.is_valid():
        company.save()

    context = {
        'company': company,
    }
    return render(request, "add_company.html", context)


def list_company(request):
    companys =  Company.objects.all()
    context = {
        "companys": companys
    }
    return render(request, "list_company.html", context)


def  company_details(request):
    pass


