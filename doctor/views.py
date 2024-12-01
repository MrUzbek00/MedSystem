from django.shortcuts import render,redirect
from django.urls import reverse
from utils.models import Appointment,Notes,PatientFiles,RegisteredPatients,Department
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from user.models import Patient,Doctor
from django.db.models import Q

@login_required(login_url='user:login')
def dashboard(request,doc_id=None):

    if request.user.department.all().exists() and not doc_id:
        return redirect(reverse('doc:head_dashboard'))
    
    if doc_id:
        doctor = Doctor.objects.get(id = doc_id)
    else:
        doctor = request.user

    now = timezone.now()
    apps = Appointment.objects.filter(date__year = now.year, date__day = now.day, doctor = doctor, active = 'active').order_by('status')
    id = request.GET.get('id',None)
    if id:
        app = Appointment.objects.get(id = id)
        app.status = True
        app.save()
        return redirect(reverse('doc:dashboard'))
    context = {
        "appointments":apps
    }
    return render(request,'doctor/doctor_dashboard.html',context)


def head_dashboard(request):
    now = timezone.now()
    doctors = Doctor.objects.filter(department_doctors = request.user.department.first())
    ward_patient = RegisteredPatients.objects.filter(Q(ward__department = request.user.department.last())).count()
    appointments = Appointment.objects.filter(date__year = now.year, date__day = now.day, doctor = request.user, active = 'active', status = False)[:4]

    context = {
        'doctors':doctors,
        'ward_patient':ward_patient,
        'appointments':appointments,
    }

    return render(request,'doctor/head_dashboard.html',context)


@login_required(login_url='user:login')
def appointments(request):
    now = timezone.now()
    apps = Appointment.objects.filter(date__year = now.year, date__day = now.day, doctor = request.user, active = 'active').order_by('status')
    id = request.GET.get('id',None)
    if id:
        app = Appointment.objects.get(id = id)
        app.status = True
        app.save()
        return redirect(reverse('doc:dashboard'))
    context = {
        "appointments":apps
    }
    return render(request,'doctor/doctor_dashboard.html',context)


@login_required(login_url='user:login')
def doctors(request):
    docs = Doctor.objects.filter(department_doctors = request.user.department.first())

    context = {
        'doctors':docs
    }

    return render(request,'doctor/specialists.html',context)

    
def ward_patient(request):
    patients = RegisteredPatients.objects.filter(Q(ward__department = request.user.department.last()) | Q(ward__department__in = request.user.department_doctors.all()))
    wards = patients.values('ward__room_number').distinct()
    ward,department = request.GET.get('ward',None),request.GET.get('department',None)
    if ward:
        patients = patients.filter(ward__room_number = ward)
    if department:
        patients = patients.filter(ward__department__name = department)
    context = {
        'patients':patients,
        'wards':wards,
    }
    return render(request,'doctor/ward_patients.html',context)


def patient_details(request,id):
    patient = Patient.objects.get(id = id)
    now = timezone.now()
    past_appointments = Appointment.objects.filter(date__year__lte = now.year, date__day__lte = now.day, patient = patient,doctor = request.user ,status = True)
    upcoming_appointments = Appointment.objects.filter(date__year__gte = now.year, date__day__gte = now.day, patient = patient,doctor = request.user ,status = False)
    notes = Notes.objects.filter(patient = patient)
    files = PatientFiles.objects.filter(patient = patient   )

    context = {
        'patient':patient,
        'past_appointments':past_appointments,
        'upcoming_appointments':upcoming_appointments,
        'notes':notes,
        'files':files,
    }
    return render(request,'doctor/details.html',context)