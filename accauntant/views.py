from django.shortcuts import render
from utils.models import Invoice,Service,Department
from user.models import Patient,Doctor
from django.utils import timezone


def dashboard(request):
    now = timezone.now()
    invoices = Invoice.objects.filter(created_date__month = now.month)
    serivces = Service.objects.all().count()
    patients = Patient.objects.all().count()
    doctors = Doctor.objects.all().count()

    departments = Department.objects.all()

    date,status,department = request.GET.get('date',None),request.GET.get('satus',None),request.GET.get('department',None)
    

    if status:
        invoices = invoices.filter(status = status)
    if department:
        selected_department = Department.objects.get(name = department)
        invoices = invoices.filter(
                    appointment__doctor__department=selected_department
                )
    if date:
        invoices = invoices.filter(created_date__date=date)

    context = {
        "invoices":invoices,
        "serivces":serivces,
        "patients":patients,
        "doctors":doctors,
        "departments":departments,
    }

    return render(request,'accauntant/accauntant.html',context)


#sizga
def paid_invoice(request,id):
    return render(request,'accauntant/passed_invoice.html')