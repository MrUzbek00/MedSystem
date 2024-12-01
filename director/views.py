from django.shortcuts import render
from user.models import Doctor,Patient,CustomUser
from utils.models import Department,Ward,Appointment,Service,RegisteredPatients
from django.db.models.functions import TruncMonth
from django.utils import timezone
from django.db.models import Count
from datetime import timedelta

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
    return render(request,'director/director_dashboard.html',context)

def staticsts(request):
    now = timezone.now()
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    wards = Ward.objects.all()
    department = Department.objects.all()
    appointments = Appointment.objects.filter(date__gte = now, status = False)
    users = CustomUser.objects.all()
    services = Service.objects.all()

    start_date = timezone.now() - timedelta(days=365)

    # Fetch data for the past 12 months and group by truncated month
    monthly_counts = Patient.objects.filter(registered_date__gte=start_date) \
                                    .annotate(truncated_month=TruncMonth('registered_date')) \
                                    .values('truncated_month') \
                                    .annotate(patients_count=Count('id'))

    # Initialize lists to store truncated month names and patient counts
    month_names = []
    patients_count = []

    # Iterate through the monthly counts and populate lists
    for entry in monthly_counts:
        month_names.append(entry['truncated_month'].strftime('%B'))
        patients_count.append(entry['patients_count'])

    region_counts = Patient.objects.values('region') \
                                       .annotate(patient_count=Count('id')) \
                                       .order_by('region')

    # Extract regions and patient counts from the query results
    regions = [entry['region'] for entry in region_counts]
    patient_count = [entry['patient_count'] for entry in region_counts]


    specialization_counts = Doctor.objects.exclude(specialization__isnull=True) \
                                                .values('specialization') \
                                                .annotate(appointment_count=Count('appointment_doctor')) \
                                                .order_by('specialization')

    # Extract specializations and appointment counts from the query results
    specializations = [entry['specialization'] for entry in specialization_counts]
    app_count = [entry['appointment_count'] for entry in specialization_counts]

    context = {
        'doctors':doctors,
        'patients':patients,
        'wards':wards,
        'department':department,
        'appointments':appointments,
        'users':users,
        'services':services,
        'month': month_names,
        'patients_count': patients_count,
        'regions': regions,
        'patient_count': patient_count,
        'specializations': specializations,
        'app_count': app_count,
    }

    return render(request,'director/statistics.html',context)
