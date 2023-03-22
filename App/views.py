from django.shortcuts import render
# imports
from django.contrib.auth.decorators import login_required
from App.models import Patient
from django.contrib import  messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator

def frontend(request):
    return render(request, "frontend.html")


# ----------------BACKEND--------------------
@login_required(login_url="login")
def backend(request):
    if 'q' in request.GET:
        q = request.GET['q']
        all_patient_list = Patient.objects.filter(
            Q(name__icontains=q) | Q(phone__icontains=q) | Q(email__icontains=q) | Q(age__icontains=q) | Q(gender__icontains=q) |
            Q(note__icontains=q)
        ).order_by('created_at')
    else:
        all_patient_list = Patient.objects.all().order_by('-created_at')

    paginator = Paginator(all_patient_list, 5)
    page = request.GET.get('page')
    all_patient = paginator.get_page(page)

    return render(request, 'backend.html', {'patients': all_patient})

@login_required(login_url="login")
def add_patient(request):
    if request.method == "POST":
        patient = Patient()
        patient.name = request.POST.get('name', None)
        patient.phone = request.POST.get('phone', None)
        patient.email = request.POST.get('email', None)
        patient.age = request.POST.get('age', None)
        patient.gender = request.POST.get('gender', None)
        patient.note = request.POST.get('note', None)
        if patient.name and patient.phone and patient.email and patient.age and patient.gender and patient.note:
            patient.save()
            messages.success(request, "Пациент добавлен!")
            return HttpResponseRedirect('/backend')
    return render(request, 'add.html')


@login_required(login_url="login")
def patient(request, patient_id):
    patient = Patient.objects.get(id = patient_id)
    if patient !=None:
        return render(request, "edit.html", {'patient': patient})

