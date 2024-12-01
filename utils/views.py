from django.shortcuts import redirect,render
from django.contrib import messages
from django.urls import reverse
from user.models import Patient
from .forms import DepartmentForm,WardForm,AppointmentForm,RegisterPatient,NotesForm,FileForm
from django.contrib.auth.decorators import login_required
from .models import Invoice
from django.http import HttpResponse
from openpyxl import Workbook
from django.db.models import Sum
from django.utils import timezone

def add_department(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"department added")
        else:
            messages.add_message(request,messages.ERROR,form.errors)
    return redirect(url)

def add_ward(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        form = WardForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"ward added")
        else:
            messages.add_message(request,messages.ERROR,form.errors)
    return redirect(url)

def add_appointment(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appo = form.save()
            invoice = Invoice.objects.create(appointment = appo,status='unpaid')
            if request.user.user_type == 'patient':
                return render(request,'client/payment_form.html',{'invoice':invoice})
            messages.add_message(request,messages.SUCCESS,"Invoice added")
        else:
            messages.add_message(request,messages.ERROR,form.errors)
    return redirect(url)

def add_patient_to_ward(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        form = RegisterPatient(request.POST)
        if form.is_valid():
            ward = form.save(commit=False)
            ward.patient = Patient.objects.get(passport_id = request.POST.get('patient_id'))
            ward.ward.book_ward
            ward.save()
            messages.add_message(request,messages.SUCCESS,"Patient registered added")
        else:
            messages.add_message(request,messages.ERROR,form.errors)
    return redirect(url)

def add_note(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect(url)

def add_file(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        form = FileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return redirect(url)


@login_required(login_url='user:login')
def settings(request):
    if request.method == "POST":
        password = request.POST.get("password")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        user = request.user

        if not password1 == password2:
            messages.add_message(request,messages.SUCCESS,"error old password is not match")    
            return render(request,'settings.html')

        if not user.check_password(password):
            messages.add_message(request,messages.SUCCESS,"error old password is not match")
            return render(request,'settings.html')
        
        user.set_password(password1)
        user.save()

    return render(request,'settings.html')


def generate_report(request):
    if request.method == "POST":
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')

        if date1 and date2:
            invoices = Invoice.objects.filter(updated_date__range=[date1, date2])
        else:
            print('hhhh')
            now = timezone.now()
            invoices = Invoice.objects.filter(created_date__year = now.year,created_date__month = now.month,created_date__day = now.day)

        # Create Excel workbook
        wb = Workbook()
        ws = wb.active

        # Define headers for the Excel sheet
        headers = ["Date", "Appointment ID", "Doctor", "Services", "Type", "Status", "Payment Type", "Amount"]
        ws.append(headers)

        # Iterate over each invoice and retrieve related data
        for invoice in invoices:
            # Extract data from the invoice and related objects
            appointment_id = invoice.appointment.id
            doctor_name = invoice.appointment.doctor.get_full_name()
            services = ", ".join(service.name for service in invoice.appointment.services.all())
            appointment_type = invoice.appointment.type
            invoice_status = invoice.status
            payment_type = invoice.payment_type
            amount = invoice.appointment.services.aggregate(total_cost=Sum('cost'))['total_cost'] if invoice.appointment.services.exists() else 0

            # Add data to Excel sheet
            ws.append([
                invoice.updated_date.strftime("%Y-%m-%d"),  # Invoice updated date
                appointment_id,
                doctor_name,
                services,
                appointment_type,
                invoice_status,
                payment_type,
                amount
            ])

        # Save workbook to response
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=invoice_report.xlsx'
        wb.save(response)
        return response

# Create your views here.
