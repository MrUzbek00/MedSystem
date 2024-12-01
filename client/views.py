from django.shortcuts import render,redirect
from django.urls import reverse
from utils.models import Appointment,Department,Service,Notes,PatientFiles,Invoice
from django.contrib.auth.decorators import login_required
from user.models import Doctor
from .decorators import is_registered
from django.contrib import messages
from user.forms import UserUpdateForm

@login_required(login_url='user:login')
def dashboard(request):
    appointments = Appointment.objects.filter(patient = request.user)
    context = {
        "appointments":appointments
    }
    return render(request,'client/my_appointments.html',context)

@login_required(login_url='user:login')
@is_registered
def new_appointment(request,doctor_id=None):
    if doctor_id:
        doctor_id = Doctor.objects.get(id = doctor_id)
    
    doctors = Doctor.objects.all()
    services = Service.objects.all()
    
    context = {
        "doctor":doctor_id,
        "doctors":doctors,
        "services":services,
    }
    
    return render(request,'client/new_appointment.html',context)

def doctors(request):
    doctors_list = Doctor.objects.all()
    departments = Department.objects.all()

    gender,department = request.GET.get('gender',None),request.GET.get('department',None)

    if gender:
        doctors_list = doctors_list.filter(gender = gender)
    if department:
        doctors_list = doctors_list.filter(department__name = department)
        
    context = {
        'doctors':doctors_list,
        'departments':departments,
    }

    return render(request,'client/doctors.html',context)

def make_payment(request,id):

    invoice = Invoice.objects.get(id = id)

    if request.method == 'POST':
        invoice.payment_type = 'card'
        invoice.status = 'paid'
        invoice.appointment.active = 'active'
        invoice.appointment.save()
        invoice.save()
        return redirect(reverse('cl:dashboard'))


    context = {
        'invoice':invoice
    }
    return render(request,'client/payment_form.html',context)

@login_required(login_url=('user:login'))
def client_details(request):

    notes = Notes.objects.filter(patient = request.user)
    files = PatientFiles.objects.filter(patient = request.user)

    context = {
        'notes':notes,
        'files':files
    }

    return render(request,'client/details.html',context)

@login_required(login_url=('user:login'))
def update_profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST,request.FILES,instance = request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('cl:client_details'))
        else:
            messages.add_message(request,messages.WARNING,form.errors)
    return render(request,'client/update.html')