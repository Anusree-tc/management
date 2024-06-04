from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import BookingForm
from .models import Departments, Doctors, Patient
from .forms import PatientForm


# Create your views here.

def index(request):
    return render(request, 'index.html')


def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            patients = Patient.objects.all()
            return render(request, 'patient.html', {'patients': patients})
    form = BookingForm()
    dict_form = {
        'form': form
    }
    return render(request, 'booking.html', dict_form)


def doctors(request):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }

    return render(request, 'doctors.html', dict_docs)


def department(request):
    dict_dept = {
        'dept': Departments.objects.all()
    }
    return render(request, 'department.html', dict_dept)


def patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient')
    else:
        form = PatientForm()
    dict_pat = {
        'form': form,
        'patients': Patient.objects.all()
    }
    return render(request, 'patient.html',dict_pat)


def contact(request):
    return render(request, 'contact.html')
