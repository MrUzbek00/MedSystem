from django.shortcuts import render
from user.models import Doctor,Patient,CustomUser
from utils.models import Department,Ward,Appointment,Service,RegisteredPatients
# from ..user.models import Doctor
from django.db.models import F



def dashboard(request):

    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    wards = Ward.objects.all()
    department = Department.objects.all()
    appointments = Appointment.objects.filter(status = False)

    context = {
        'doctors':doctors,
        'patients':patients,
        'wards':wards,
        'department':department,
        'appointments':appointments,
    }


    return render(request,'adminstration/dashboard.html',context)

def add_department(request):
    doctors = Doctor.objects.all()
    
    context = {
        'doctors':doctors
    }

    return render(request,'adminstration/add_department.html',context)

def add_patient(request):
    return render(request,'adminstration/add_patient.html')

def add_doctor(request):
    return render(request,'adminstration/add_specialist.html')

def appaintments(request):
    appointments = Appointment.objects.all().order_by('status')

    type = request.GET.get('type',None)

    if type:
        appointments = appointments.filter(type = type)

    context = {
        'appointments':appointments
    }

    return render(request,'adminstration/appointments.html',context)

def new_appointment(request):

    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    services = Service.objects.all()

    context = {
        'doctors':doctors,
        'patients':patients,
        'services':services,
    }

    return render(request,'adminstration/new_appointment.html',context)

def patients(request):

    patients = Patient.objects.all()

    context = {
        'patients':patients
    }

    return render(request,'adminstration/patients.html',context)

def register_to_ward(request):
    wards = Ward.objects.filter(number_booked__lt = F('number_patients'))
    patients = Patient.objects.all()

    context = {
        'wards':wards,
        'patients':patients
    }

    return render(request,'adminstration/register_to_wards.html',context)

def doctors(request):
    doctors_list = Doctor.objects.all()
    departments = Department.objects.all()

    gender,department = request.GET.get('gender',None),request.GET.get('department',None)

    if gender:
        doctors_list = doctors_list.filter(gender = gender)
    if department:
        doctors_list = doctors_list.filter(department_doctors__name=department)


    context = {
        "doctors":doctors_list,
        "departments":departments,
    }
    return render(request,'adminstration/specialists.html',context)

def ward_patients(request):
    patients = RegisteredPatients.objects.all()
    wards = patients.values('ward__room_number').distinct()
    departments = Department.objects.all()

    ward,department = request.GET.get('ward',None),request.GET.get('department',None)

    if ward:
        patients = patients.filter(ward__room_number = ward)
    if department:
        patients = patients.filter(ward__department__name = department)

    context = {
        'patients':patients,
        'wards':wards,
        'departments':departments,
    }

    return render(request,'adminstration/ward_patients.html',context)

def wards(request):
    departments = Department.objects.all()
    wards = Ward.objects.all()

    context = {
        'departments':departments,
        'wards':wards,
    }

    return render(request,'adminstration/wards.html',context)
